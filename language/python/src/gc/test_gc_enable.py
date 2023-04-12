""" 逻辑类似test_gc_leak, 但开启gc.enable, 此时仍然存在一定的内存泄漏, 但是会在达到一定的值之后不再增长

注意: 这种内存上限也不固定, 会突然的内存突破上限, 然后过一会儿就突然降低, 这样会造成内存使用的极大不稳定性
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

class ClassA:
    def __init__(self):
        used_mem = psutil.Process(os.getpid()).memory_info().rss / 1024.0 / 1024.0
        print(f'新的对象生成, id: {str(hex(id(self)))}, garbage: {len(gc.garbage)}, '
              f'计数器: {gc.get_count()}, 当前总内存:{used_mem}MB')
        self.values = copy.deepcopy(Values)

    def __del__(self):
        pass


def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        #  del c1
        #  del c2
        time.sleep(1)


gc.enable()
print(f'--------垃圾回收自动执行频率: {gc.get_threshold()}')  # 一般为: (700, 10, 10)
f2()
