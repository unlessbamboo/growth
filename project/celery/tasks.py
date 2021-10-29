""" 最简单的异步任务
1. celery命令详情:
    格式: celery [OPTIONS] COMMAND [ARGS]
    options:
        -A/--app 应用
        -b/--broker 中间人
        -l/--loglevel 日志等级
        -Q/--queues 执行消息队列名
        -c/--concurrency 同时处理任务的工作进程数量, 默认为可用CPU数量
        -n/--hostname 设置自定义主机名
        -B/--beat 定义运行celery周期任务调度程序

    COMMAND
        worker 启动worker实例
            celery -A proj worker -l debug
        status 查看集群内所有活跃的节点
            celery -A proj status
        purge 从任务队列中撤销消息, 永久删除消息
            celery -A proj purge (删除所有待处理任务)
        control worker实例远程控制 
            celery -A proj control enable_events 开启任务事件
            celery -A proj control disable_events 关闭任务事件
        inspect 检查worker runtime信息
            celery -A proj inspect active 列出正在执行的任务
            celery -A proj inspect scheduled 列出定时任务
            celery -A proj inspect reserved 列出被worker领取但是未执行的任务, 不包含定时任务
            celery -A proj inspect revoked 列出取消的任务
            celery -A proj inspect registered 列出注册的任务
            celery -A proj inspect stats 进行数据统计

"""
from celery import Celery

# a. celery程序或应用:
#   a. 首参数为当前模块名
#   b. broker(中间人): 消息中间件, 用于接收和发送消息, 以独立服务形式出现
#   c. backend(保存任务结果)
# b. 运行职程服务(worker): celery -A tasks worker --loglevel=info
app = Celery('tasks', broker='redis://127.0.0.1:6379/10', backend='redis://127.0.0.1:6379/9')


@app.task
def add(valuea, valueb):
    """ 后续通过ipython启动一个异步任务
        from tasks import add
        add.delay(4, 4)
    """
    return valuea + valueb
