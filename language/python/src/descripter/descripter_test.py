# coding:utf-8
"""
1. 描述符协议: 一个新式类一旦定义了:
    __get__(self, instance, owner): self为描述符对象实例, instance描述符作用的对象实例, owner描述符作用的类
    __set__(self, instance, value): value为实际赋值
    __delete_(self, instance)
该类就会被称为descripter(描述符), 上面的定义就是一个描述符协议.
注意, descripter是一个对象(有点蒙蔽是吧?), 一般作为其他类对象属性而存在.

2. 用途: 通过对控制属性实现: 
    + 计算属性: 类似vue的computed, 通过__get__来返回特定的计算值, 见proxy_test.py
    + 懒加载
    + 属性访问控制

3. 限制: 
    a. 描述符在属性查找过程中会被 . 点操作符调用，且只有在作为类变量使用时才有效, 
        所以必须把描述符定义成这个类的类属性，不能定义到构造函数中

4. descripter类型
    + data descripter: 实现了__set__或者__delete__的任一方法
    + non-data descripter: 仅实现__get__方法
    他们的行为: 
        + 数据描述符总是会覆盖实例字典 __dict__ 中的属性
        + 非数据描述符可能会被实例字典 __dict__ 中定义的属性所覆盖
    具体见nondata_test.py

5. 使用场景: 
    a. python为弱类型语言, 通过定义Type描述符来增加类型限制
    b. 绑定行为: 在属性get,set,del的时候做一些值的合法性判断, 打印字符等等额外操作.
    c. 托管属性: 利用描述符(类)去托管owner的相关属性, 一种代理机制, 见下面的性格类, 重量类.

6. 对象属性访问顺序(object.__getattribute__()源码):
    a. 实例属性
    b. 类属性
    c. 父类属性
    d. __getattr__方法

7. python内部的描述符
    a. property: 类似vue的计算属性语法糖, 这是一个实现了描述符协议的类, 见property_test.py
    b. 函数: 每一个我们定义的函数对象都是一个non-data描述符实例
    c. classmethod: 这是函数描述符基础上的一个变种
    c. staticmethod: 

参考: https://waynerv.com/posts/python-descriptor-in-detail/
"""
from __future__ import print_function
import types
import requests


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

    @property
    def score(self):
        """ property:相当于声明了score属性，另外还有@property.getter和setter、deleter的声明 """
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
    @前期知识：
        1,类中所有的函数都是non-data descripter，返回bound或者unbound方法
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

    @检验步骤：
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
