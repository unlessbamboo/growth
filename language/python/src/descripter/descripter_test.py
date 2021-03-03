# coding:utf-8
"""
一个新式类一旦定义了:
    __get__(self, instance, owner): instance使用描述符类实例, owner使用描述符类
    __set__(self, instance, value)
    __delete_(self, instance)
    中任何一个方法, 该类就会被称为descripter(描述符).
descripter分为: data descripter, non-data descripter.
注意, descripter(类)是一个对象(有点蒙蔽是吧?), 一般作为其他类对象属性而存在.

@绑定行为: 在属性get,set,del的时候做一些值的合法性判断, 打印字符等等额外操作.
@托管属性: 利用描述符(类)去托管owner的相关属性, 一种代理机制, 见下面的性格类,
    重量类.

@1 对象属性访问顺序:
    a. 实例属性(实际上就是调用默认的__getattribute__方法
    b. 类属性
    c. 父类属性
    d. __getattr__方法

测试descipter的某些简单功能:
    1，descripter是属性、实例方法、静态方法、类方法、super的实现机制
"""
from __future__ import print_function
import types
import requests


class CharacterDescriptor(object):
    """ 描述性格的专用类 """
    def __init__(self, value):
        self._value = value

    def __get__(self, instance, owner):
        print('性格: get')
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise Exception('xxxxxx')
        self._value = value


class NumDescriptor(object):
    def __init__(self, number):
        self._num = number

    def __get__(self, instance, owner):
        return self._num

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise Exception('xxxxxxx')


class TestDescipter(object):
    """TestDescipter"""

    def __init__(self, name):
        """__init__

        :param name: Object's name
        """
        self.name = name
        self._score = 0

    def testMethod(self):
        """testMethod"""
        print('testMeothd:{0}'.format(self.name))

    @classmethod
    def classmyMethod(cls):
        print('classMethod!')

    ##
    # @brief    property:相当于声明了score属性，另外还有
    #               @property.getter和setter、deleter的声明
    #
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        """score:使用property修饰

        :param value:
        """
        if not isinstance(value, int):
            raise Exception('xxx')
        self._score = value

    @score.getter
    def score(self):
        """score:使用property修饰"""
        self._score += 1
        return self._score


def methodTest():
    """methodTest:测试method是如何建立在func的基础之上的。
        前期知识：
            1,类中所有的函数都是non-data descripter，返回bound或者
            unbound方法
            2,方法调用
                aObj.f
                等价于：
                aObj.__dict__['fun1'].__get__(aObj, type(aObj))
                其中__get__方法定义如下：
                class Function:
                    def __get__(self, obj, objtype=None):
                        return types.MethodType(self, obj, objtype)
                其中self表示函数实例，MethodType返回方法类型，例如：
                    <bound method dict.items of {'age': 3}>
            3,func是一个non-data descripter
            4,方法的转换：
                普通方法：f(*args) ---> f(obj, *args)
                静态方法：f(*args) ---> f(*args)
                类方法：f(class, *args) --> f(type(obj), *args)

        检验步骤：
            1，输出方法对象本身，输出type(obj).__dict__['func'].__get__(obj, cls),
                比对结果
            2，输出类方法本身，输出Cls.__dict__['func'].__get__(None, cls),
                比对结果
            3，从而验证property的本质：
                调用方法，本身就是使用__get__调用；
                调用类方法，本身就是使用__get__调用呢，参数不同而已

    """
    test1 = TestDescipter('test1')
    print('对象调用(验证相等)-方法对象打印:{0}\n\t方法类型：{1}'.format(
        test1.testMethod,
        types.MethodType(test1.testMethod, test1, type(test1))))
    print('对象调用__dict__[...]输出:{0}'.format(
        TestDescipter.__dict__['testMethod'].__get__(test1, TestDescipter)))
    print('类调用-方法对象打印:{0}'.format(
        TestDescipter.classmyMethod))
    print('类调用__dict__[...]输出:{0}'.format(
        TestDescipter.__dict__['classmyMethod'].__get__(None, TestDescipter)))
    print('使用@property，逐渐递增score值：\n')
    print('Score value:{0}, {1}, {2}, {3}'.format(
        test1.score, test1.score, test1.score, test1.score))


if __name__ == '__main__':
    methodTest()
