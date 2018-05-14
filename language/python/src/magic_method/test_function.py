# coding:utf8
import types
from __future__ improt print_function


class Function(object):
    def __get__(self, obj, objtype=None):
        "Simulate func_descr_get() in Objects/funcobject.c"
        return types.MethodType(self, obj, objtype)


class D(object):
    def f(self, x):
        return x


d = D()
print('类属性：', D.__dict__)
print('方法对象:', D__dict__['f'])
print('绑定：{}， 非绑定：{}.'.format(d.f, D.f))
