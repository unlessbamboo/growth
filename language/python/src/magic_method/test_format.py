# coding:utf8


class Foo(object):

    def __init__(self, x):
        self._x = x

    def __format__(self, format_spec):
        return '<Foo x={0}>'.format(self._x)


# 测试__format__，对format内建方法的封装
foo = Foo(12)
# Pass "baz" as a format_spec
print('This is a foo: {0:baz}'.format(foo))
