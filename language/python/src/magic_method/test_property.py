# coding:utf8
from __future__ import print_function


class Property(object):
    """
    Emulate PyProperty_Type() in Objects / descrobject.c
    该类时Property的python实现方式
    参考: https: // stackoverflow.com / questions / 17330160 / how - does - the - property - decorator - work
    """

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        """通过装饰器语法糖来修饰欲装饰属性，返回一个property实例对象本身"""
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class TestProperty(object):
    def __init__(self):
        self._name = 'kuang'

    @property
    def name(self):
        print('我是descriptor，装饰器property.')
        return self._name

    @name.setter
    def name(self, value):
        """
            其中name.setter返回property对象，装饰器是一个语法糖，相当于如下调用:
                name.setter(name)
            此时name.setter(name).fget == name
        """
        self._name = value

    def me(self, name):
        print('Name:', name)


testObj = TestProperty()
print('实例拥有的属性值:', testObj.__dict__)
print('类拥有的属性值：', TestProperty.__dict__)
