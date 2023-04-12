""" 非永真循环中, 自动释放 """
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

    def __del__(self):
        """ 即使在del中调用了该逻辑, 但是gc不会主动调用该函数, 所以仍然无效, 只有主动调用gc.collect()
            此时才会调用del函数
        """
        if hasattr(self, 'recycleobj'):
            print('--------1')
            obj = self.recycleobj
            self.recycleobj = None
            if hasattr(obj, 'recycleobj'):
                obj.recycleobj = None


def f2_nowhile():
    """ 即使退出函数作用域, 内存还是仍然未释放, 这个很重要, 所以循环引用不可取 """
    c1 = ClassA()
    c2 = ClassA()
    c1.recycleobj = c2
    c2.recycleobj = c1
    del c1
    del c2
    time.sleep(1)


# 此时没有主动调用gc.collect()进行处理, 会发现内存的使用一直在增加
while True:
    f2_nowhile()
print('-------end--------')
