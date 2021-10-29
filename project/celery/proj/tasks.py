"""
运行职程: celery -A proj worker -l debug
程序调用测试:
    方法1: add.delay(2, 2)
    方法2: add.apply_async((2, 2)), 另外还可以指定执行参数: 运行时间, 队列

AsyncResult:
    delay/apply_async会返回AsyncResult对象, 用于跟踪任务状态
    结果后端(backend): 默认情况下, 若未配置backend, 则禁用结果, 此时无法跟踪

任务:
    ID: 每一个task都有一个唯一UUID, 唯一的name(add.name)
    STATUS: 任务状态
        PENDING -> STARTED -> SUCCESS
        PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS
        PENDING -> STARTED -> FAILED
        PENDING -> STARTED -> REVOKED
    名字:
        名称组成方式: 模块路径名.函数名
        任务名字一般是根据导入路径自动生成的, 后续都是依赖该名字来进行查找,故
        其他模块使用该task的时候需要确保导入路径是一致的:
            from proj.myapp.tasks import aTask
            from .myapp.tasks import aTask
        上面两种方式都是没问题的, 如果碰到名字不同的情况, 则可以显示的指定task name:
            @task(name='proj.myapp.tasks.add')
            def add(x, y):
                return x + y
        重写自动命名机制:
            from celery import Celery
            class MyCelery(Celery):
                def gen_task_name(self, name, module):
                    pass
            app = MyCelery('main')
    角色:
        a. 定义调用任务时发生的事情, 例如: 发送消息
        b. worker收到消息后应该发生的事件(回调)
    异常处理:
        worker会提前订阅消息(爬虫项目中碰到), 一旦worker被kill或断电, 这些消息
        会被传递给其他worker
    幂等: 
        worker无法检测任务是幂等的
        - 默认: 执行任务前确认消息, 避免多个worker之前一个任务
        - acks_late: 任务幂等时可以设置该选项, worker在执行任务之后确认消息
        任务执行异常退出都会导致确认消息的发生(sys.exit, 信号等), 避免重复执行错误的task,
        占用资源

    注册表:
        所有的任务都在注册表中(app.tasks), 其中包含task name和task:
            from proj.celery import app
            app.tasks  # {'celery.chord_unlock': <@task: celery_chork_unlock>}
        另外还有内置的task, 相关模块被导入的时候就会导入这些inline task.
        另外, app.task()装饰器会将task注册到task register中

签名: 将task signature传递给另外一个进程, 或者作为其他函数参数
    add.signature((2, 2), countdown=10)
    add.s(2, 2)
    a. 搭配签名使用delay:
        s1 = add.s(2, 2)
        res = s1.delay()
    b. 搭配并使用partials偏函数功能:
        s1 = add.s(2)  # add(?, 2)
        res = s2.delay(8)  # add(8, 2)

签名相关原语:
    groups: 一个组并行调用task list, 返回一个special AsyncResult
        a. 签名
            from celery import group
            g = group(add.s(i, i) for i in xrange(10))
            g().get()  # [0, 2, 4, 6, ...]
        b. partials
            from celery import group
            g = group(add.s(i) for i in xrange(10))
            g(10).get()

    chains: 将任务链接在一起, 在一个返回之后调用链上下一个任务
        例子:
            from celery import chain
            from proj.tasks import add, mul
            chain(add.s(4, 4) | mul.s(8))().get()  # (4 + 4) * 8
            或
            (add.s(4, 4) | mul.s(8))().get()
    chords: 和弦, 一个带有回调的组
        例子:
            from celery import chord
            from proj.tasks import add, xsum
            chord((add.s(i, i) for i in xrange(10)), xsum.s())().get()

路由: 将消息发送到指定的任务队列中
    a. task_routes: 设置一个按照名称分配的路由任务队列
    b. 指定消费任务队列 
        add.apply_async((2, 2), queue='hzmcq')
        或指定职程从哪里消费任务
        celery -A proj worker -Q hzmcq,drccq

远程控制: 在运行时控制和检查职程(worker)
    a. 职程正在处理任务(广播消息, 所有worker收到并回复): celery -A proj inspect active
    b. 指定目的地: celery -A proj inspect active --destination=celery@exp.com
    c. 状态: celery -A proj status 
    d. 控制: celery -A proj control enable_events

任务请求: celery.Task.request, 包含与当前执行任务相关的message, status等
    属性: 
        id, group, chord(和弦ID), args, kwargs, origin(发送任务主机), hostname(worker节点名),
        root_id(任务所属工作流中第一个任务ID), parent_id(调用此任务的任务ID)
    获取:
        @app.tasks(bind=True)
        def dump_context(self, x, y):
            print(self.request)

日志:
    worker会自动记录日志信息, 也可以手动配置日志记录, 通过继承方式来获取日志中的name, id.
    a. 正常用例
        from celery.utils.log import get_task_logger
        logger = get_task_logger(__name__)

        @app.task
        def add(x, y):
            logger.info(f'Adding {x} + {y}')
            return x + y
    b. 重定向日志
        import sys
        from celery.utils.log import get_task_logger

        logger = get_task_logger(__name__)

        @app.task(bind=True)
        def add(self, x, y):
            old_outs = sys.stdout, sys.stderr
            rlevel = self.app.conf.worker_redirect_stdouts_level
            try:
                self.app.log.redirect_stdouts_to_logger(logger, rlevel)
                return x + y
            finally:
                sys.stdout, sys.stderr = old_outs

重试:
    a. 任务执行错误时, 可以手动通过celery.Task.retry重新执行:
        > 发送与原始任务相同的ID消息, 发送到原始任务队列中
        > 
            @app.task(bind=True)
            def send_twitter_status(self, oauth, tweet):
                try:
                    twitter = Twitter(oauth)
                    twitter.update_status(tweet)
                except (Twitter.FailWhaleError) as exc:
                    raise self.retry(exc=exc)
            注意, retry()调用会自动引发异常, 表示worker需要重试任务.
            exc: 传递日志和存储任务结果时的异常信息
    b. 自定义重试延时(默认3分钟)
        @app.task(bind=True, default_retry_delay=3 * 60)
        def add(self, x, y):
            try:
                pass
            except Exception as exc:
                raise self.retry(exc=exc, countdown=60)
"""
from .celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task(bind=True)
def add_bind(self, x, y):
    """ 绑定任务: 首参数即任务实例
    @使用场景:
        重试(app.Task.retry), 访问当前任务信息, 添加到自定义任务基类等功能
    """
    return x + y


@app.task
def multiple_handler(x, y):
    """ 在一个任务中等待任务的结果, 这样可能导致死锁, 下面就是错误例子 """
    sum_value = xsum.delay(x, y).get()
    mul_value = mul.delay(x, y).get()
    return True


def multiple_handler_correct(x, y):
    """ 使用链的方式来达到multiple_handler的效果 """
    chain = xsum.s(x, y) | mul.s(x, y)
    chain()
