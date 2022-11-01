""" 代码对象 """
from util import show_function  # pylint: disable=import-error
import os
import sys

COMMON_PATH = os.path.abspath(os.path.dirname(
    os.path.dirname(__file__))) + os.sep + 'common'
sys.path.insert(0, COMMON_PATH)


global_name = 'global'


@show_function(desc='代码对象-闭包')
def fun1():
    name = 'fun1'

    def fun2():
        age = 1

        def fun3():
            nonlocal age
            age += 1
            print(f'名字: {name}, 全局: {global_name}, 年龄:{age}')

        print('打印最里层函数的作用域信息:')
        for attr in dir(fun3.__code__):
            if attr.startswith('co_'):
                print(f"{attr}:\t{getattr(fun3.__code__, attr)}")
        return fun3

    print('打印第二层函数作用域信息:')
    for attr in dir(fun2.__code__):
        if attr.startswith('co_'):
            print(f"{attr}:\t{getattr(fun2.__code__, attr)}")
    print('\n\n')
    return fun2


fun1()
