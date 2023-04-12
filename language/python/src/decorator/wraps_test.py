""" 在大部分场景中有没有functools.wraps函数都不影响装饰器的实现, 但是建议所有的装饰器都增加该字段

@functool.wraps用途: 在扩展功能函数的同时保留该原有函数的各种属性:
    + __name__
    + __doc__
    等等

参考: https://blog.csdn.net/misayaaaaa/article/details/102762472
"""
from functools import wraps


def Singleton(cls):
    """ 这是一个装饰器的doc """
    _instance = {}

    def inner():
        """ 装饰器内部inner doc """
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


def SingletonWraps(cls):
    """ 这是一个装饰器的doc """
    _instance = {}

    @wraps(cls)
    def inner():
        """ 装饰器内部inner doc """
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


@Singleton
class AClass:
    """ 这是原有A类的doc """
    def __init__(self):
        self.name = 'bifeng'


@SingletonWraps
class BClass:
    """ 这是原有B类的doc """
    def __init__(self):
        self.name = 'bifeng'


if __name__ == '__main__':
    print('1. 无wraps装饰的原有类的__doc__值:')
    print(AClass.__doc__)
    print()

    print('2. 有wraps装饰的原有类的__doc__值:')
    print(BClass.__doc__)
    print()
