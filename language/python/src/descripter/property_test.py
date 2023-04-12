""" 实现一个类似python内部描述符property的描述符类 """

class MyProperty:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):  # 描述符协议方法
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)  # fget: 即property(实际为property.getter)修饰的函数

    def __set__(self, obj, value):  # 描述符协议方法
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)  # fset: 即func.setter修饰的函数

    def __delete__(self, obj):  # 描述符协议方法
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)  # fdel: 即func.deleter修饰的函数

    def getter(self, fget):  # 实例化一个拥有 fget 属性的描述符对象
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):  # 实例化一个拥有 fset 属性的描述符对象
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):  # 实例化一个拥有 fdel 属性的描述符对象
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class CTest:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = MyProperty(getx, setx, delx, "I'm the 'x' property.")


class NormalTest:
    def __init__(self):
        self._name = 'bifengNormalTest'

    @MyProperty
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print(f'Name的setter被调用:{value}')
        self._name = value

    @name.deleter
    def name(self):
        print(f'Name的deleter被调用')
        del self._name


if __name__ == '__main__':
    print('-------测试property自定义实现-------')
    ct = CTest()
    print(f'赋值前: {ct.x}')

    ct.x = 'bifeng'
    print(f'赋值后: {ct.x}')
    print()

    print('-------装饰器使用---------')
    nobj = NormalTest()
    print(nobj.name)
    print()

    nobj.name = 'newvalue'
    print(nobj.name)
    print()

    del nobj.name
