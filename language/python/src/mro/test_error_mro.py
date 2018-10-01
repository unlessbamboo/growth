# coding:utf8


class X(object):
    pass


class Y(object):
    pass


class A(X, Y):
    pass


class B(Y, X):
    """最终会在这里提示冲突"""
    pass


class C(A, B):
    def __init__(self):
        super(C, self).__init__(self)
        print('C')


c = C()
