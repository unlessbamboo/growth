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


@show_function(desc='作用域-静态作用域')
def scope_static_verify():
    name = 'global'

    def fun1():
        print(f'被调用函数fun1, 此时name值:{name}')

    def fun2():
        name = 'fun2'
        fun1()

    fun2()


@show_function(desc='作用域-重新定义和引用外部变量')
def redefine_outer_variable_verify():
    """ 类似javascript代码:
            function func() {
                var num = 0;
                function inner() {
                    var num = num + 1;  // undefined + 1 == NaN
                }
                return inner;
            }
            func()();
    """
    def _do():
        num = 0

        def inner():
            """ num被赋值, interpreter认为num是一个局部变量, 故而报错 """
            print(f'执行函数时局部变量字典locals值:{locals()}')
            num = num + 1  # noqa: F823, pylint: disable=used-before-assignment
            return num
        co = inner.__code__
        print(f'函数(inner)预制的局部变量名: {co.co_varnames}, 非局部:{co.co_names}')
        return inner
    do = _do()
    do()


scope_name = 'global'


@show_function(desc='作用域-作用域链测试')
def scope_link_verify():
    """ 作用域链, 在代码编写的时候决定, 其中javascript的作用域是存储在函数变量对象的[[scope]]
    数组中, Python 则存储在函数``__closure__``魔术属性中, 其也是一个数组
    """
    scope_name = 'link'

    def scope_inner():
        scope_name = 'inner'

        def show():
            scope_num = 0

            def show_inner():
                print(scope_name, '--', scope_num)
            return show_inner

        return show

    def scope_closure():
        print(f'My Scope Name:{scope_name}')

    show_inner = scope_inner()
    in2 = show_inner()
    return scope_closure


@show_function(desc='作用域-作用域链测试')
def scope_test():
    pass


if __name__ == '__main__':
    import inspect
    global_info = globals()
    for k in list(global_info):
        func = global_info.get(k)
        if '_verify' in k and inspect.isfunction(func):
            func()
