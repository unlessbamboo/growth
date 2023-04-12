""" 非永真循环中

注意: 此情况下, 即使不手动gc, 也会在内存达到400MB左右再进行释放
"""
import os
import sys
import copy
import time
import gc
import psutil
import objgraph


a = "hello world"
sys.getrefcount(a)
Values = [{'name': i, 'age': i} for i in range(10000)]

class ClassA():
    def __init__(self):
        used_mem = psutil.Process(os.getpid()).memory_info().rss / 1024.0 / 1024.0
        print(f'新的对象生成, id: {str(hex(id(self)))}, 当前总内存:{used_mem}MB')
        self.values = copy.deepcopy(Values)


def f2_nowhile():
    """ 即使退出函数作用域, 内存还是仍然未释放, 这个很重要, 所以循环引用不可取 """
    c1 = ClassA()
    c2 = ClassA()
    c1.t = c2
    c2.t = c1
    del c1
    del c2
    time.sleep(1)


# 此时没有主动调用gc.collect()进行处理, 会发现内存的使用一直在增加
number = 0
while True:
    f2_nowhile()
    if number % 50 == 0:
        objgraph.show_most_common_types(limit=50) 
    number += 1
print('-------end--------')
