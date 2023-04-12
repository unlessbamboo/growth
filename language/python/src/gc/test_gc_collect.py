""" 逻辑类似test_gc_leak, 但是主动调用gc.collect

现象: 最大使用内存一直维持在一定的量, 不会导致大范围的内存泄漏

触发垃圾回收时机:
    + 显示调用gc.collect(), 其返回不可达的对象数目并放入garbage列表中
    + gc的计数器达到阈值的时候
    + 程序退出的时候

函数: 
    1、gc.set_debug(flags) 设置gc的debug⽇志，⼀般设置为gc.DEBUG_LEAK
    2、gc.collect([generation]) 显式进⾏垃圾回收，可以输⼊参数
        + 0 代表只检查第⼀代的对象
        + 1 代表检查⼀，⼆代的对象
        + 2 代表检查⼀，⼆，三代的对象，如果不传参数，执⾏⼀个full collection，也就是等于传2。

        返回不可达(unreachable objects)对象的数⽬

    3、gc.get_threshold() 获取的gc模块中⾃动执⾏垃圾回收的频率, 其默认值为(700, 10, 10):
        
        + 在G0的对象数量达到700之前, 不把未被回收的对象放入G1
        + 在G1的对象数量达到10之前, 不把未被回收的对象放入G2
        
    4、gc.set_threshold(threshold0[, threshold1[, threshold2]) 设置⾃动执⾏垃圾回收的频率。
    5、gc.get_count() 获取当前⾃动执⾏垃圾回收的计数器，返回⼀个⻓度为3的列表。

        a. 值: (488, 3, 0): 488表示从上一次一代垃圾检查到现在剩余待释放内存数目(总分配内存数目 - 已释放数目) 
        b. 释放
            当计数器从(699,3,0)增加到(700,3,0)，执⾏gc.collect(0),即检查⼀代对象的垃圾，并重置计数器
            当计数器从(699,9,0)增加到(700,9,0)，执⾏gc.collect(1),即检查⼀、⼆代对象的垃圾，并重置计数器
            当计数器从(699,9,9)增加到(700,9,9)，执⾏gc.collect(2),即检查⼀、⼆、三对象的垃圾，并重置计数器

        --> 分代收集原理: 刚出生为G0, 在一轮GC扫描下存活, 移动到G1, 再次扫描存活(G1), 移动到G2

触发时机:
    + 引用计数: 
        优点: 简单, 极为方便的触发, 内存释放块
        缺点: 
            循环引用: 见test_circular_ref.py

    + 标记-清除: 
        优点: 解决循环引用, 通过从root节点开始遍历, 将所有可访问对象打上标记, 对于未标记对象则进行清理
        缺点: 但是不知道何时会触发, 非常不稳定
        根节点: 全局静态变量, 当前帧栈中本地变量表中引用的对象, 见test_sign.py

    + 分代收集原理: 在执行GC回收的时候程序会被暂停, 为了减少暂停时间而提出了分代回收以降低垃圾回收耗时
        世代: G0, G1, G2

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
        print(f'新的对象生成, id: {str(hex(id(self)))}, garbage: {len(gc.garbage)}, '
              f'计数器: {gc.get_count()}, 当前总内存:{used_mem}MB')
        self.values = copy.deepcopy(Values)


def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        gc.collect()
        time.sleep(1)


# 此时没有主动调用gc.collect()进行处理, 会发现内存的使用一直在增加, 但达到一定上限之后停止(不一定)
gc.enable()
f2()
