from collections import deque


class ActorScheduler:
    """ 角色调度器 """

    def __init__(self):
        self._actors = {}          # Mapping of names to actors
        self._msg_queue = deque()   # Message queue

    def new_actor(self, name, actor):
        """
        Admit a newly started actor to the scheduler and give it a name
        """
        # 一个新的角色(任务), 这些角色会行使其职责范围内的某些任务
        self._msg_queue.append((actor, None))
        self._actors[name] = actor

    def send(self, name, msg):
        """
        Send a message to a named actor
        """
        # 向某一个角色发送一个任务
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        """
        Run as long as there are pending messages.
        """
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)  # 向特定的任务发送某个符合条件的数据, 类似 OS 将挂起进程唤醒并发送某些重要数据
            except StopIteration:
                pass


def printer():
    while True:
        msg = yield  # 打印机挂起任务, 等待数据过来, 有数据就打印数据
        print('Got:', msg)


def counter(sched):
    while True:
        n = yield  # 等待一个"计数任务"
        if n == 0:  # 计数结束, 迭代结束
            break
        # Send to the printer task
        sched.send('printer', n)
        # Send the next count to the counter task (recursive)
        sched.send('counter', n - 1)


if __name__ == '__main__':
    sched = ActorScheduler()
    # Create the initial actors
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))
    # Send an initial message to the counter to initiate
    sched.send('counter', 10000)  # 调度器任务
    sched.run()
