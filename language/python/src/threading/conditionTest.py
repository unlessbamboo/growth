# coding:utf8
""" Condition线程通知事件测试 """
import time
import threading


class ConditionTimer(object):
    def __init__(self, interval):
        """ 一个定时器线程, 在超时后发送信号, 唤醒所有等待该条件的线程. """
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        """ 确保定时器以后台线程方式运行 """
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        #  定时器, 无限循环
        while True:
            time.sleep(self._interval)
            with self._cv:  # 语法糖, 获取锁
                self._flag ^= 1  # 或非操作, 5^2==7, 5^1==4, 3^1==2
                self._cv.notify_all()  # 通知

    def wait_for_tick(self):
        """ 等待定时器通知 """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:  # 或非操作, 实际上就是一个轮回
                self._cv.wait()  # 该函数底层会自动释放锁


def count_down(ptimer, nticks):
    """ 滴答递减操作 """
    while nticks > 0:
        ptimer.wait_for_tick()
        print('Count Down 滴答:', nticks)
        nticks -= 1


def count_up(ptimer, nticks):
    """ 滴答递增操作 """
    n = 0
    while n < nticks:
        ptimer.wait_for_tick()
        print('Count up 加加:', n)
        n += 1


if __name__ == '__main__':
    # 启动定时器
    ptimer = ConditionTimer(1)
    ptimer.start()
    # 启动滴答
    p1 = threading.Thread(target=count_down, args=(ptimer, 10))
    p1.start()
    p2 = threading.Thread(target=count_up, args=(ptimer, 5))
    p2.start()
    p1.join()
    p2.join()
    print('**' * 5)
