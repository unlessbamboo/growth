""" 线程基本测试, 创建一个计数线程 """
import time
import threading


class CountDownTask(object):
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('时间:', n)
            n -= 1
            time.sleep(1)


if __name__ == '__main__':
    c = CountDownTask()
    t = threading.Thread(target=c.run, args=(10,))
    t.start()
    time.sleep(3)
    c.terminate()
    t.join()
    print('=' * 10)
