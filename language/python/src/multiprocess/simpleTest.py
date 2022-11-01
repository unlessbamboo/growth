# coding:utf-8
import os

import multiprocessing


def func1(arg1, arg2, arg3):
    """传入三个参数"""
    print("args1:", arg1)
    print("args2:", arg2)
    print("args3:", arg3)
    print('进程名:{}'.format(multiprocessing.current_process().name)


if __name__ == "__main__":
    """main"""
    p2=multiprocessing.Process(target=func1, args=(3, 4, 5))
    p2.start()
    p2.join()
    print("p2, end")
