""" 测试内存泄漏值

@观察: 通过htop -p PID可以看到进程的内存使用一直在增加
"""
import os
import sys
import copy
import time
import gc
import psutil


a = "hello world"
sys.getrefcount(a)
Values = [{'name': i, 'age': i} for i in range(10000)]

class ClassA():
    def __init__(self):
        used_mem = psutil.Process(os.getpid()).memory_info().rss / 1024.0 / 1024.0
        print(f'新的对象生成, id: {str(hex(id(self)))}, 当前总内存:{used_mem}MB')
        self.values = copy.deepcopy(Values)


def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        time.sleep(1)


# 此时没有主动调用gc.collect()进行处理, 会发现内存的使用一直在增加
f2()
