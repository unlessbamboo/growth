---
title: celery队列阻塞问题记录
description: "celery默认队列阻塞: 阻塞原因, 影响其他任务, 后续解决
date: 2021-10-20 17:03:07

---


#### 1. 基础知识
1. docker命令集

```txt
sudo docker exec -ti drcc-docker_drcc-backend_1 bash

# celery beat启动
celery -A app.worker.celery beat --loglevel=info --scheduler app.worker:LockedPersistentScheduler
```


2. supervisor任务

```sh
supervisorctl start drcc
supervisorctl start drcc-beat
supervisorctl start drcc-celery
supervisorctl start drcc-db-pairs
supervisorctl start drcc-db-pairs-detect
supervisorctl start drcc-mon
supervisorctl start drcc-switch
```


3. flower

基于web的监控和管理Celery的工具:

+ celery事件实时监控: 进程及历史, 进程详细信息, 图形化统计
+ worker状态和统计
+ 关闭和重启worker实例
+ 平滑配置, 控制进程池大小
+ 查看/修复一个worker消费队列
+ 查看当前正在运行中的tasks
+ 查看计划任务
+ 撤销和终止任务


#### 2. 问题定位
tip1: 系统时间快了8个小时, 实际时间17:36, 系统时间: 23:06

1. 查看supervisorctl服务状态: ``supervisorctl status``, 状态正常
2. 导出docker日志: ``docker logs drcc-docker_drcc-backend_1 > stderr.log 2>&1``, 暂时未看出大的问题
3. 手动触发各类异步任务, 查看相关日志是否有任务触发, 发现手动触发任务未触发
4. 判断celery任务是否存在僵死, 重启现象: ``ps -ef | grep 'celery -A app.worker.celery worker -c 10 --loglevel=info'``

```txt
# UID          PID    PPID  C STIME(进程启动时间) TTY(中断)          TIME(总进程时间, 启动进程之后占用进程累计时间) CMD(命令)
okp       115249       1  0 Oct19 ?        00:07:06 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info

okp       136856  115249  0 10:05 ?        00:00:00 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info
okp       137531  115249  0 11:00 ?        00:00:00 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info
okp       141586  115249  0 16:58 ?        00:00:00 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info
okp       141887  115249  0 17:23 ?        00:00:01 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info
okp       141898  115249  0 17:24 ?        00:00:02 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info
okp       141922  115249  0 17:26 ?        00:00:00 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info
okp       141939  115249  0 17:27 ?        00:00:00 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info
okp       141974  115249  0 17:31 ?        00:00:00 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info
okp       141975  115249  0 17:31 ?        00:00:00 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info
okp       141995  115249  0 17:32 ?        00:00:00 /home/okp/.pyenv/versions/3.6.5/envs/drcc-backend-env/bin/python3.6 /home/okp/.pyenv/versions/drcc-backend-env/bin/celery -A app.worker.celery worker -c 10 --loglevel=info
```

可以看到主进程(115249)中控进程, 所有CPU占用时间都在该进程中.

5. 判断是否redis服务未提供: ``ping drcc-redis``
6. 查看docker容器内存是否不足: ``free -h``

```txt
              total        used        free      shared  buff/cache   available
Mem:            15G        6.9G        180M         48M        8.3G        8.0G
Swap:          2.0G         59M        1.9G
total: 脚本内存总量, 即物理内存
used: 内容使用量(正在被使用中)
free: 多少空闲区
buff/cache: 用作内核缓存的物理内存量
```

参考: [celery rabbitmq内存异常](https://daimajiaoliu.com/daima/4796cff999003fc), 但是这里使用redis作为backend,
而且内存也没有任何不足现象.

7. 查看celery worker的状态: ``celery -A app.worker.celery status``

```txt
->  celery@d94b96e72034: OK
->  celery@d94b96e72034: OK
->  celery@d94b96e72034: OK
->  celery@d94b96e72034: OK
->  celery@d94b96e72034: OK

..warning..

1 node online.
```

+ 第一栏: 表示5个worker运行中, 其默认的命名方式: ``workername@hostname``, 如果名字相同会有warning信息
+ 第二栏: worker计数(不同名)

8. 查看当前正在运行中的task: ``celery -A app.worker.celery inspect active``, 判断是否有大量任务堆积

```txt
->  celery@d94b96e72034: OK
    - empty -
->  celery@d94b96e72034: OK
    * ...a
    * ...b
->  celery@d94b96e72034: OK
    - empty -
->  celery@d94b96e72034: OK
    - empty -
->  celery@d94b96e72034: OK
    * ...1
    * ...2
    * ...3
```

其中每一个task会展示所有待处理任务.

9. 查看当前活动队列的信息: ``celery -A app.worker.celery inspect active_queues``

```txt
->  celery@d94b96e72034: OK
    * {'name': 'drcc-db-pairs-detect', 'exchange': {'name': 'drcc-db-pairs-detect', 'type': 'direct', 'arguments': None, 'durable': True, 'passive': False, 'auto_delete': False, 'delivery_mode': None, 'no_declare': False}, 'routing_key': 'drcc-db-pairs-detect', 'queue_arguments': None, 'binding_arguments': None, 'consumer_arguments': None, 'durable': True, 'exclusive': False, 'auto_delete': False, 'no_ack': False, 'alias': None, 'bindings': [], 'no_declare': None, 'expires': None, 'message_ttl': None, 'max_length': None, 'max_length_bytes': None, 'max_priority': None}
->  celery@d94b96e72034: OK
    * {'name': 'celery', 'exchange': {'name': 'celery', 'type': 'direct', 'arguments': None, 'durable': True, 'passive': False, 'auto_delete': False, 'delivery_mode': None, 'no_declare': False}, 'routing_key': 'celery', 'queue_arguments': None, 'binding_arguments': None, 'consumer_arguments': None, 'durable': True, 'exclusive': False, 'auto_delete': False, 'no_ack': False, 'alias': None, 'bindings': [], 'no_declare': None, 'expires': None, 'message_ttl': None, 'max_length': None, 'max_length_bytes': None, 'max_priority': None}
->  celery@d94b96e72034: OK
    * {'name': 'drcc-db-pairs', 'exchange': {'name': 'drcc-db-pairs', 'type': 'direct', 'arguments': None, 'durable': True, 'passive': False, 'auto_delete': False, 'delivery_mode': None, 'no_declare': False}, 'routing_key': 'drcc-db-pairs', 'queue_arguments': None, 'binding_arguments': None, 'consumer_arguments': None, 'durable': True, 'exclusive': False, 'auto_delete': False, 'no_ack': False, 'alias': None, 'bindings': [], 'no_declare': None, 'expires': None, 'message_ttl': None, 'max_length': None, 'max_length_bytes': None, 'max_priority': None}
->  celery@d94b96e72034: OK
    * {'name': 'drcc-switch-or-ttx', 'exchange': {'name': 'drcc-switch-or-ttx', 'type': 'direct', 'arguments': None, 'durable': True, 'passive': False, 'auto_delete': False, 'delivery_mode': None, 'no_declare': False}, 'routing_key': 'drcc-switch-or-ttx', 'queue_arguments': None, 'binding_arguments': None, 'consumer_arguments': None, 'durable': True, 'exclusive': False, 'auto_delete': False, 'no_ack': False, 'alias': None, 'bindings': [], 'no_declare': None, 'expires': None, 'message_ttl': None, 'max_length': None, 'max_length_bytes': None, 'max_priority': None}
->  celery@d94b96e72034: OK
    * {'name': 'drcc-mon', 'exchange': {'name': 'drcc-mon', 'type': 'direct', 'arguments': None, 'durable': True, 'passive': False, 'auto_delete': False, 'delivery_mode': None, 'no_declare': False}, 'routing_key': 'drcc-mon', 'queue_arguments': None, 'binding_arguments': None, 'consumer_arguments': None, 'durable': True, 'exclusive': False, 'auto_delete': False, 'no_ack': False, 'alias': None, 'bindings': [], 'no_declare': None, 'expires': None, 'message_ttl': None, 'max_length': None, 'max_length_bytes': None, 'max_priority': None}

```

10. 当前worker内存占用: ``celery -A app.worker.celery inspect memdump``, 该功能依赖psutil模块

11. 当前worker的统计信息: ``celery -A app.worker.celery inspect stats``

12. 清空队列: ``celery -A app.worker.celery purge`` 或者 ``celery -A app.worker.celery purge -Q queue_name``

13. 队列内部内容信息: ``redis-cli -h host1 -p PORT -n number0 keys *``

```txt
1) "_kombu.binding.drcc-mon"
2) "_kombu.binding.celeryev"
3) "_kombu.binding.celery"
4) "_kombu.binding.drcc-switch-or-ttx"
5) "_kombu.binding.drcc-db-pairs-detect"
6) "_kombu.binding.drcc-db-pairs"
7) "_kombu.binding.celery.pidbox"
```

查看任务队列(默认)目前堆积个数: ``llen celery``
清空任务队列: ``ltrim celery 0 0``
