""" 测试最简单的函数装饰器和解析

注意: @就是一个语法糖, python解释器会将该修饰符解释为一个封装逻辑
引申: 由下面的例子可以引申中单例函数装饰器的使用原理

使用场景: 
    + 缓存
    + 代理
    + 上下文环境
    + 日志

设计模式: 代理模式, 装饰器模式
"""


def Singleton(cls):
    """ 单例模式, 此时装饰器传递的就是一个cls对象 """
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


def mydecorator(func):
    """ 1. 解析和测试无参装饰器, 有参函数 """
    def inner_func(*args, **kwargs):
        print('----------begin---------')
        rsp = func(*args, **kwargs)
        print('----------end---------')
        return rsp
    return inner_func


def mydecorator_params(*dargs, **dkwargs):
    """ 2. 解析和测试有参装饰器, 有参函数 """
    # 一旦装饰器携带了参数, 那就需要多封装一层结构
    def new_decorator(func):
        def inner_func(*args, **kwargs):
            print('----------begin---------')
            print(f'装饰器参数为: {dargs}, {dkwargs}')
            rsp = func(*args, **kwargs)
            print('----------end---------')
            return rsp
        return inner_func
    return new_decorator


@mydecorator
def show_fullname(firstname, lastname):
    print(f'{firstname}-{lastname}')
    return True


@mydecorator_params('参数1', age='kwargs参数')
def show_fullname_params(firstname, lastname):
    print(f'{firstname}-{lastname}')
    return True


def origin_show_fullname(firstname, lastname):
    print(f'{firstname}-{lastname}')
    return True


def parse_decorator(*args, **kwargs):
    """ 解析上面的装饰器, 上面的装饰器就可以拆解为如下的结构 """
    f1 = mydecorator(origin_show_fullname)
    return f1(*args, **kwargs) 


if __name__ == '__main__':
    print('1. 正常的装饰函数:')
    show_fullname('zheng', 'bifeng')
    print()

    print('2. 拆解装饰器函数:')
    parse_decorator('zheng', 'bifeng')
    print()

    print('3. 正常的带参数装饰函数:')
    show_fullname_params('zheng', 'bifeng')
    print()
