# coding:utf8



class D(object):
    pass


class E(object):
    pass


class F(object):
    pass


class B(D, E):
    def show_msg(self):
        print('B show')


class C(D, F):
    def show_msg(self):
        print('c show')


class A(B, C):
    def __init__(self):
        super(A, self).__init__()
        print('A class')


a = A()
a.show_msg()
