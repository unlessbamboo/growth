# coding:utf8
"""
1. 创建职程worker: celery -A {workername} worker --loglevel=info

2. 启动客户端并发布一个task message:
    from tasks import add
    add.delay(3, 4)

3. task任务, 存在两种角色:
    a. 定义了调用任务时发生的事情(发送消息)
    b. worker收到任务消息时该发生的事件
   每一个任务都有task_id, 一旦某一个worker被kill或者断电, 则会自动将所有task
   转移到其他worker中.

4. 确认消息: worker在收到确认消息之前, 不会主动从队列中删除对应任务消息.
"""

from celery import Celery


# 使用redis作为broker: 模块名, broker路径
app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y
