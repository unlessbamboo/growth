from collections import deque


def countdown(n):
    """ 任务 1 """
    while n > 0:
        print('T-minus', n)
        yield  # 任务挂起(条件不允许的时候挂起)
        n -= 1
    print('Blastoff!')


def countup(n):
    """ 任务 2: 变量处于闭合状态 """
    x = 0
    while x < n:
        print('Counting up', x)
        yield  # 任务挂起
        x += 1


class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        """
        Admit a newly started task to the scheduler
        """
        self._task_queue.append(task)

    def run(self):
        """
        Run until there are no more tasks
        """
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)  # 获取task中的数据直到yield, 条件允许了, 可以将某一个挂起任务执行了
                self._task_queue.append(task)
            except StopIteration:
                # Generator is no longer executing
                pass


# 目标: 创建一个调度器, 然后并行处理三个任务(通过queue来共享)
sched = TaskScheduler()
sched.new_task(countdown(10))
sched.new_task(countdown(5))
sched.new_task(countup(15))
sched.run()
