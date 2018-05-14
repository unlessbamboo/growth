# coding:utf8
from __future__ import print_function


class Desc(object):
    """Desc本身就是一个描述符，因为存在__get__, __set__方法"""

    def __get__(self, instance, owner):
        print("__get__...")
        # 输出<DESC.object>，实例对象x
        print("self : \t\t", self)
        # 输出<TestDesc.object>，即t
        print("instance : \t", instance)
        # 输出<class.TestDesc>
        print("owner : \t", owner)
        print('=' * 40, "\n")

    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('=' * 40, "\n")


class TestDesc(object):
    x = Desc()


"""
    以下为测试代码，在查找x时，发现为类属性，同时定义了描述器，
    则descriptor会将TestDesc.x转变为TestDesc.__dict__['x'].__get__(None, TestDesc)来访问
"""
t = TestDesc()
t.x
