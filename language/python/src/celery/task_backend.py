# coding:utf8
"""
存储celery的任务执行结果, 下面的任务执行之后会生成如下的执行结果
key: celery-task-meta-be7169cd-e2fa-4c8d-9b55-7edd8f0b7622
value(字符串):
   {
        "status": "SUCCESS",
        "date_done": "2021-04-20T05:00:59.738880",
        "task_id": "be7169cd-e2fa-4c8d-9b55-7edd8f0b7622",
        "traceback": null,
        "result": "This is a backend test",
        "children": []
    }

2. 发送一个任务并获取任务结果
    from task_backend import backend
    t1 = backend.delay()
    t2 = backend.delay()
    t1.get(timeout=3)
    t2.get(timeout=3)
    # 将t2存储结果释放
    t2.forget()
   在完成上述的操作只会, redis仅仅存储t1任务结果信息(TTL默认为一天)
"""
from __future__ import print_function
from celery import Celery


app = Celery('task_backend', broker='redis://localhost:6379/1',
             backend='redis://localhost:6379/8')


@app.task
def backend():
    s1 = 'This is a backend test'
    print(s1)
    return s1
