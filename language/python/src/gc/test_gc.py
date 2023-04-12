# coding: utf8
"""
功能: 测试python的垃圾回收在循环引用中的处理机制

说明1: 如果循环引用中，两个对象都定义了__del__方法，gc模块不会销毁这两个不可达对象，因为gc模块不知道应该先调用哪个对象的__del__方法.
    ---> python3中不管是否定义del方法, 都会导致循环引用, 无法释放问题

参考: https://www.cnblogs.com/zzbj/p/13532156.html
注意: 该问题只在python2(老版本, GC引用计数版本)中才出现

    + python2: 引用计数--无法解决循环引用的问题, 所以干脆不处理存在__del__的类释放

参考: https://www.cnblogs.com/zzbj/p/13532156.html
"""
from __future__ import print_function
import sys
import gc
import time

class Teacher:
    def __init__(self):
        self.Stu = None
        

class Student:
    def __init__(self):
        self.Tea = None
    

def test_recycle(level=0):
    """ 测试循环引用 """
    tea = Teacher()
    stu = Student()
    
    #设置循环引用
    tea.Stu = stu
    stu.Tea = tea
    print(f'对象tea的引用计数:{sys.getrefcount(tea)}')
    del tea
    del stu
    
    # 执行垃圾回收, 返回值: 处理这些循环引用一共释放掉的对象个数
    print('开始内存回收...')
    _unreachable = gc.collect(level)
    print(f'开始执行一次垃圾回收, 返回值: {_unreachable}')
    print(f'内存泄露(garbage)的对象个数: {gc.garbage}')
    

if __name__ == '__main__':  
    """
    命令(将标准错误重定向/dev/null): python3 syntax/test_gc.py 2 2>/dev/null
    """
    # reachable: 可访问对象, unreachable对象: collectable-可回收, uncollectable-不可回收
    gc.enable()  # 启用垃圾回收, 停止: disable()
    #  gc.set_debug(gc.DEBUG_LEAK)  # 设置垃圾回收的调试标志位, 此方式会输出过多额外信息, 不建议
    gc.set_debug(gc.DEBUG_SAVEALL)  # DEBUG_SAVEALL: 所有不可访问对象存放至 gc.garbage 列表中
    
    if len(sys.argv) <= 1 or sys.argv[1] == '0':
        print('-----------测试第0代垃圾回收-------------')
        test_level(0)
    elif sys.argv[1] == '1':
        print('-----------测试第1代垃圾回收-------------')
        test_level(1)
    elif sys.argv[1] == '2':
        print('-----------测试第2代垃圾回收-------------')
        test_level(2)
    
    time.sleep(3)
    gc.disable()
    print('程序退出!')
