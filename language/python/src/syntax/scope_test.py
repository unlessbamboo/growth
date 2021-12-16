"""
功能: 作用域测试
知识点: 
    1. 作用域是静态的, 变量名被赋值的位置决定了变量能够被访问的范围(javascrip也是, 预解析的时候就决定了)
    2. 作用域: 模块, 类, 函数中才会产生, 目前没有块作用域的概念
"""
import os
import sys

COMMON_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + os.sep + 'common'
sys.path.insert(0, COMMON_PATH)
from util import show_function  # pylint: disable=import-error


@show_function(desc='作用域-测试是否存在块作用域')
def scope_classify_verify():
    """ 作用域分类LEGB, python的作用域类似javascript, 不存在块级作用域 """
    # 1. 访问for循环内部定义的变量
    num = 0
    for _ in range(3):
        num += 1
        name = 'for scope'
    print(f'num:{num}, name值: {name}')


@show_function(desc='作用域-重新定义和引用外部变量')
def redefine_outer_variable_verify():
    num = 0

    def inner():
        # 这里代码执行会报错, 类似javascript, 因为num被赋值, 故而python认为num是一个
        # 全局变量, 然后就会报错: local variable 'num' referenced before assignment
        num = num + 1
        return num

    return inner


scope_name = 'global'


@show_function(desc='作用域-作用域链测试')
def scope_link_verify():
    """ 作用域链, 类似javascript, Python 也有一个作用域链, 其在代码编写的
    时候就已经决定了, 其中javascript的作用域是存储在函数变量对象的[[scope]]
    数组中, Python 则存储在函数``__closure__``魔术属性中, 其也是一个数组
    """
    scope_name = 'link'

    def scope_inner():
        scope_name = 'inner'
        clo = scope_inner.__closure__
        print(f'链长度:{len(clo)}')
        for ele in clo:
            print(ele.cell_contents)

    def scope_closure():
        print(f'My Scope Name:{scope_name}')

    scope_inner()
    return scope_closure


if __name__ == '__main__':
    #  # 1. 作用域分类
    #  scope_classify()
    #  
    #  redefine_outer_variable()
    #  
    #  # 2. 作用域链
    #  scope_link()()
    import inspect
    global_info = globals()
    for k in list(global_info):
        func = global_info.get(k)
        if '_verify' in k and inspect.isfunction(func):
            func()
