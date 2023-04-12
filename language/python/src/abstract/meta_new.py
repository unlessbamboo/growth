""" 
功能: 测试type和type.__new__的区别
"""

class MetaA(type):
    """ 1. 通过type创建返回的新类和MetaA没有任何关系, 此时不会调用__init__进行初始化 """
    def __new__(cls, name, bases, dct):
        print('MetaA.__new__')
        return type(name, bases, dct)

    def __init__(self, name, bases, dct):
        print('MetaA.__init__')


class A(metaclass=MetaA):
    pass


class MetaB(type):
    """ 2. 通过type.__new__创建返回的新类会调用__init__进行初始化 """
    def __new__(cls, name, bases, dct):
        print('MetaB.__new__')
        return type.__new__(cls, name, bases, dct)

    def __init__(self, name, bases, dct):
        print('MetaB.__init__')


class B(metaclass=MetaB):
    pass


if __name__ == '__main__':
    print('-------------type创建的新类-----------')
    print(MetaA.__new__)
    print()

    print('-------------type.__new__创建的新类-----------')
    print(MetaB.__new__)
    print(MetaB.__init__)
    print()
