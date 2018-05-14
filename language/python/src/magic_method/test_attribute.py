# coding:utf8
"""
    测试魔术方法中的属性访问控制
"""
from __future__ import print_function


class TestNotExistedAttr1(object):
    """测试当重载__getattribute__时没有手动调用__getattr__的的输出"""

    def __getattr__(self, name):
        print("__getattr__")

    def __getattribute__(self, name):
        print("__getattribute__")


class TestNotExistedAttr2(object):
    """测试当重载__getattribute__时自动调用__getattr__的的输出"""

    def __getattr__(self, name):
        print("__getattr__")

    def __getattribute__(self, name):
        print("__getattribute__")
        super(TestNotExistedAttr2, self).__getattribute__(name)


class TestSetAttribute1(object):
    def __init__(self):
        self.count = 0

    def __setattr__(self, name, value):
        print("递归错误、如果name为count，还会产生未定义错误")
        self.name = value


t1 = TestNotExistedAttr1()
t2 = TestNotExistedAttr2()
# 访问不存在属性
print("手动调用时:")
t1.x
print("\n\n自动调用时:")
t2.x
