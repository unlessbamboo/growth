""" 配置和初始化

主名称(main): celery进行任务消息传递时, worker通过task name来进行交互, 这称为task register(装饰器默认注册)
    from proj.tasks import add
    add  # 输出: <@task: tasks.add>

配置:
    1. 例子:
        timezone: 时区
        enable_utc: utc
    2. 加载查询顺序: 
        a. 运行时所作更改
        b. 配置模块
        c. 默认配置(celery.app.default)
    3. 加载配置config_from_object
        from celery import Celery
        app = Celery()
        app.config_from_object('celeryconfig')

        celeryconfig.py:
            enable_utc = True
            timezone = 'Asia/Shanghai'
    4. 配置模块对象
        from celery import Celery
        app = Celery()

        class Config:
            enable_utc = True
            timezone = 'Asia/Shanghai'

        app.config_from_object(Config)
    5. 从环境变量中获取配置: config_from_envvar
    6. 过滤配置(敏感信息): app.config.humanize(with_defaults=False, censored=True)

    7. 任务decorator配置
        Task.name: 任务注册名称
        Task.request: 任务请求信息
        Task.max_retries: 重试最大次数(异常时不会自动重试, 需要手动调用retry)
        Task.throws: 预期内的异常, 仅仅记录结果到后端, 但是不会记录为错误信息, 无回溯信息
        Task.relat_limit: 指定时间内任务运行的数量(每一个worker)
        Task.time_limit: 任务硬时间限制
        Task.soft_time_limit: 任务软时间限制
        Task.backend: 结果后端, 便于后续的检索, RPC结果后端: 消息发送, 数据库结果后端
        Task.acks_late: 幂等任务的处理

创建并初始化的流程:
    1. 创建用于event的逻辑时钟实例
    2. 创建task注册表
    3. 将自身设置为当前应用程序
    4. 调用app.on_init()回调函数, 注意app.task() decorator不会在定义task时创建任务,
        一般在使用该task或者应用程序完成后创建任务
    判断任务是否创建:
        from celery import Celery
        app = Celery('proj', broker='redis://127.0.0.1:6379/10')

        @app.task
        def add(x, y):
            return x + y
        type(add)  # <class 'celery.local.PromiseProxy'>

        add.__evaluated__()  # False
        add   # 使用add, 但未调用任务
        add.__evaluated__()  # True
    实例是懒加载, 创建一个实例只会将app设置为current_app, 当调用app.finalize()或访问app.tasks时才完成
"""
from celery import Celery, Task


# 创建celery实例
#   broker: 中间人
#   backend: 结果存储后端URL
#   include: 程序启动时倒入的模块列表, 一般在此处添加任务模块, 以便后续worker处理相应任务
# 线程安全: 配置多个app在同一个进程中运行
app = Celery('proj', broker='redis://127.0.0.1:6379/10',
             backend='redis://127.0.0.1:6379/9', include=['proj.tasks'])

# 增加配置项(运行时所作配置更改)
app.conf.update(
    result_expires=3600,
)


class DebugTask(Task):
    """ 自定义任务类
    使用方式1:
        @app.task(base=DebugTask)
        def add(x, y):
            return x + y
    使用方式2(全局改动):
        from celery import Celery
        app = Celery('proj', broker='redis://127.0.0.1:6379/10')

        app.Task = DebugTask
        @app.task
        def add(x, y):
            return x + y
        add
        add.__class__.mro()  # 输出

    一个任务在内部默认形式:
        @app.task
        def add(x, y):
            return x + y

        --自动转为(celery.local.PromiseProxy, add也存在run方法)-->

        class _AddTask(app.Task):
            def run(self, x, y):
                return x + y
        add = app.tasks[_AddTask.name]  # 注册表

    actor: 并行计算模式中的概念, 一个actor对接收的消息做出响应并进行本地决策,
        在处理完之后准备接收下一条消息.

    实例化(重要):
        任务并非对每一个消息或请求进行实例化, 任务实例作为全局实例在任务注册表
        中register, 每一个进程调用一次__init__, 类似actor, 例如缓存数据库连接
            from celery import Task

            class DatabaseTask(Task):
                _db = None

                @property
                def db(self):
                    if self._db is None:
                        self._db = Database.connect()
                    return self._db
            
            @app.task(base=DatabaseTask)
            def process_rows():
                for row in process_rows.db.table.all():
                    process_row(row)
        一个函数被装饰为task, 则该task就是一个全局对象

    handlers: task返回之后的回调处理逻辑
        after_return: 任务返回后的处理
        on_failed: 任务执行失败后处理
        on_retry: 任务重试
        on_success: 任务重试
    """
    def __call__(self, *args, **kwargs):
        print(f'TASK STARTING: {self.name}[{self.request.id}]')
        return super(DebugTask, self).__call__(*args, **kwargs)

    def run(self):
        super(DebugTask, self).run()


if __name__ == '__main__':
    """
    1. 任务调用
        task的任务消息基于python消息库kombu实现, 其实现了一个客户端同rabbitmq/redis等broker
        进行交互:
            apply_async(args, kwargs, ...): 发送一个任务消息
            delay(args, kwargs): 直接发送一个任务消息, 不支持运行参数
            calling(__call__): 应用一个支持调用接口的对象, task不会被一个worker执行但会在当前线程中执行
        例子:
            T.delay(args, kwargs=value): 等价于apply_async(args, kwargs)
            T.apply_async(countdown=10):  10秒后执行
            T.apply_async(countdown=60, expires=120): 60s后执行, 但在120s后过期
            T.apply_async(expires=now + timedelta(days=2))
        delay和apply_async调用区别:
            T.delay(args1, args2, kwargs1='x', kwargs2='y')
            T.apply_async(args=[args1, args2], kwargs={'kwargs1': 'x', 'kwargs2': 'y'})
    """
    app.start()
