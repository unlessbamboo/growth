# coding:utf8
""" 测试多进程, 并加入可调用对象的测试 """
import multiprocessing
import time


class CallableFucn(object):
    """可调用对象"""

    def __init__(self, func, args):
        """init"""
        self._argsList = args
        self._func = func

    def __call__(self):
        """call"""
        self._func(*self._argsList)


def counter(n, b):
    """ 打印自身 """
    print('这是一个被可调用对象操作的子进程函数: {}'.format(n * b))
    time.sleep(2)


if __name__ == '__main__':
    # 1. 此时传递参数通过可调用对象来操作
    p1 = multiprocessing.Process(target=CallableFucn(counter, args=(3, 4)))
    p1.start()
    for _ in range(10):
        print('---主进程等待中---')
        p1.join()
    print('===============')
