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

    7. 任务decorator配置(见2.2节)
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
    2. 任务调用(calling Task)
    2.1. 任务调用
        task的任务消息基于python消息库kombu实现, 其实现了一个客户端同rabbitmq/redis等broker
        进行交互:
            apply_async(args, kwargs, ...): 发送一个任务消息
            delay(args, kwargs): 直接发送一个任务消息, 不支持运行参数
            calling(__call__): 应用一个支持调用接口的对象, task不会被一个worker执行但会在当前线程中执行
        例子:
            T.delay(args, kwargs=value): 等价于apply_async(args, kwargs)
            T.apply_async(countdown=10):  10秒后执行
            T.apply_async(countdown=60, expires=120): 60s后执行, 但在120s后过期
            T.apply_async(expires=now + timedelta(days=2))  # 立刻开始执行, 两天内过期

        delay和apply_async调用区别:
            T.delay(args1, args2, kwargs1='x', kwargs2='y')
            T.apply_async(args=[args1, args2], kwargs={'kwargs1': 'x', 'kwargs2': 'y'})
        
        签名方式:
            T.s(arg1, arg2, kwargs1='x1', 'kwargs2='y').apply_async()

        任务链:
            res = add.apply_async((2, 2), link=add.s(16))
            其中res.get()结果: 4, res.children(0).get()结果: 20, 即回调任务用父任务的结果作为部分参数,
            类似偏函数的操作逻辑.

    2.2 任务调用参数
        ETA(预计到期时间)或countdown:
            result = add.apply_async((2, 2), countdown=3)
            cesult = add.apply_async((2, 2), eta=datetime.utcnow() + timedelta(days=1))
            设置一个日期, 在该时间之前任务将被执行, 其中countdown为以秒为单位的快捷ETA方式.
            NOTE: 队列等待或者网络延时可能导致上面设置的时间点不准确, 需要提前监听队列拥塞情况.
       
        expires:
            add.apply_async((2, 2), expires=60)
            add.apply_async((2, 2), expires=datetime.now() + timedelta(days=1))
            设置到期时间, 如果worker收到过期任务, 将该task标记为TaskRevokedError

        retry以及其他重试策略(retry_policy):
            add.apply_async((2, 2), retry=False)
            消息重发, 默认情况下, 连接失败会自动重发消息, retry会直接禁止重试logic, 当然也可以
            设置重试的详细策略:
                max_retries: 最大重试次数, 抛出重试失败异常, 默认值为3, 若值为None, 表示一直重试
                interval_start: 定义两次重试之间的间隔描述, 默认值为0
                interval_step: 定义每次重试时延时, 默认为0.2
                interval_max: 定义重试之间等待的最大描述, 默认为0.2
            例子:
                add.apply_async((2, 2), retry=True, retry_policy={
                    'max_retries': 3,
                    'interval_start': 0,
                    'interval_step': 0.2,
                    'interval_max': 0.2,
                })
            重试的最长时间为0.4秒, 确保代理连接等断开之后, 因为重试导致的堆效应.

    2.3 连接池
        从2.3版本开始, 支持自动连接池, 无需开发者手动创建连接池和重用连接;
        从2.5版本开始, 默认弃用连接池;
        手动处理连接:
            results = []
            with add.app.pool.acquire(block=True) as connection:
                with add.get_publisher(connection) as publisher:
                    try:
                        for args in numbers:
                            res = add.apply_async((2, 2), publisher=publisher)
                            results.append(res)
                    except Exception as msg:
                        pass 
            print(res.get() for res in results)

    2.4 Routing Options
        将任务路由到不同的队列中: add.apply_async(queue='priority.high')
        队列: celery -A proj worker -l info -Q celery,priority.high

    2.5 调用函数
        a. 在工作进程中执行任务
            add.s(2, 2).delay()
            add.s(2, 2).apply_async(countdown=1)
        b. 在当前进程中执行任务
            add.s(2, 2)()
                
    """
    app.start()
