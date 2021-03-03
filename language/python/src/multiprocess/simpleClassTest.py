""" 派生进程多进程测试 """
import multiprocessing
import time


class MyProcess(multiprocessing.Process):
    def __init__(self, name):
        self.name = name
        super(MyProcess, self).__init__()

    def run(self):
        """ 启动函数 """
        print('派生进程:{} 准备启动中'.format(self.name))
        time.sleep(2)


if __name__ == '__main__':
    p = MyProcess('SubProcess')
    p.start()
    p.join()
    print('=====================')
