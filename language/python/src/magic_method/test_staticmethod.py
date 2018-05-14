# coding:utf8


class StaticMethod(object):
    """
        Emulate PyStaticMethod_Type() in Objects/funcobject.c
    """

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f


class ClassMethod(object):
    """
        Emulate PyClassMethod_Type() in Objects/funcobject.c
        类方法的python实现
    """

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)

        def newfunc(*args):
            return self.f(klass, *args)
        return newfunc
