# coding:utf8
""" 测试threading.Event """
import threading
import time


class TestThread(threading.Thread):
    def __init__(self, name, event):
        super(TestThread, self).__init__()
        self.name = name
        self.event = event

    def run(self):
        print('Thread: ', self.name, ' start at:', time.ctime(time.time()))
        self.event.wait()  # 等待事件被设置信号, 实际上也可以主线程等待其他线程设置标志位
        print('Thread: ', self.name, ' finish at:', time.ctime(time.time()))


if __name__ == '__main__':
    event = threading.Event()
    threads = []
    for i in range(1, 3):
        threads.append(TestThread(str(i), event))

    print('main thread start at: ', time.ctime(time.time()))
    event.clear()  # 在启动所有线程之前先置空标志位
    for thread in threads:
        thread.start()

    print('sleep 5 seconds.......')
    time.sleep(5)
    print('主线程准备设置标志位, 通知所有其他线程')
    event.set()
