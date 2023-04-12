""" 功能: 实现函数重载

参考: https://qiwsir.github.io/2020/02/26/python-overload-function/
"""
import time
from inspect import getfullargspec


class Function:
    """ 一个Function类, 对真正的函数进行包装以实现重载 """
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        """when invoked like a function it internally invokes
        the wrapped function and returns the returned value.
        """
        fn = Namespace.get_instance().get(self.fn, *args)
        if not fn:
            raise Exception("no matching function found.")

        return self.fn(*args, **kwargs)

    def key(self, args=None):
        """Returns the key that will uniquely identify
        a function (even when it is overloaded).
        """
        # if args not specified, extract the arguments from the
        # function definition
        if args is None:
            args = getfullargspec(self.fn).args

        return tuple([
          self.fn.__module__,  # 函数所述模块
          self.fn.__class__,  # 函数所述类
          self.fn.__name__,  # 函数名
          len(args or []),  # 函数参数长度
        ])


class Namespace(object):
    """ 构建虚拟命名空间, 保存所定义的所有函数
    """
    __instance = None

    def __init__(self):
        if self.__instance is None:
            self.function_map = dict()
            Namespace.__instance = self
        else:
            raise Exception("cannot instantiate a virtual Namespace again")

    @staticmethod
    def get_instance():
        if Namespace.__instance is None:
            Namespace()
        return Namespace.__instance

    def get(self, fn, *args):
        """get returns the matching function from the virtual namespace.

        return None if it did not fund any matching function.
        """
        func = Function(fn)
        return self.function_map.get(func.key(args=args))

    def register(self, fn):
        """ 通过Function封装fn并产生新的函数实例对象, 同时将老的对象存储到缓存中
        """
        func = Function(fn)  # 通过key实现了函数唯一性的区分, 即使函数同名
        print(fn.__doc__, func.key(), func)
        self.function_map[func.key()] = fn
        print(self.function_map)
        return func


def overload(fn):
    return Namespace.get_instance().register(fn)


@overload
def area(l, b):
    """ area(l, b) """
    return l * b


@overload
def area(r):
    """ area(r) """
    import math
    return math.pi * r ** 2


if __name__ == '__main__':
    print('------------begin----------')
    print(globals())
    print(f'area(3, 4)结果: {area(3, 4)}')
    print(f'area(7)结果: {area(7)}')
