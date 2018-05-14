# coding:utf8
from __future__ import print_function


class D(object):
    pass


class E(object):
    pass


class F(object):
    pass


class B(D, E):
    pass


class C(D, F):
    pass


class A(B, C):
    def __init__(self):
        super(A, self).__init__()
        print('A class')


a = A()
