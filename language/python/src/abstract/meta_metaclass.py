# coding:utf8
"""
元类: 创建类的东西, 元类就是类的类
type: 动态的创建类, 其接受类的描述作为参数并返回一个新的类. type是一个类, 可以通过继承type来自定义类的创建.

功能: 使用MetaClass类来进行类的创建, 而不是使用metaclass属性, 其中MC类继承type, 使用
    type来进行类的创建, 见meta_simpletest.py中的说明

使用方式:
    1. 通过metaclass类创建类, 见当前文件
    2. 通过type(name, bases, dict)创建新类, 并将新类作为基类, 见meta_inherit.py
    3. 通过__metaclass__来全局生效, 仅适用于python2.6, 在python3中失效

参数说明: 
    __new__(cls, *args, **kwargs): 用于创建对象, 在__init__之前被调用的特殊方法
    __init__(self, *args, **kwargs): 用于初始化对象
    
    type(object):  返回object的类型
    type(name, bases, dict): 返回一个新的类对象
        name: 类名称
        bases: 基类的元祖, 可为空
        dict: 类内定义的命名空间变量, 例如: {name1: value1}

注意, type的子类也可以使用上面的type(name, bases, dict)创建新的类
参考: https://reishin.me/python-metaclass/
"""


class UpperAttrMetaClass(type):
    def __new__(mcs, future_class_name, future_class_parents, future_class_attr):
        """__new__

        :param mcs: metaclass, 即UpperAttrMetaClass
        :param future_class_name: 类名
        :param future_class_parents: 父类
        :param future_class_attr: 属性
        """
        # 1. 过滤__属性
        attrs = ((name, value) for name, value in list(
            future_class_attr.items()) if not name.startswith('__'))

        # 2. 将所有属性变为大写
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        # 3. 创建新类
        return type(future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass2(type):
    """ 不同于UpperAttrMetaClass, 使用type.__new__来创建类实例 """
    def __new__(mcs, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in list(
            future_class_attr.items()) if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        # 复用type.__new__方法
        return type.__new__(mcs, future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass3(type):
    def __new__(mcs, name, bases, dct):
        attrs = ((name, value) for name, value in list(
            dct.items()) if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        # 实际操作同type.__new__
        return super(UpperAttrMetaclass3, mcs).__new__(mcs, name, bases, uppercase_attr)


class Foo(metaclass=UpperAttrMetaClass):
    bar = '继承metaclass'


class FooOrigin:
    bar = '原始类定义'


class FooTypeNew(metaclass=UpperAttrMetaclass2):
    bar = '继承metaclass-使用__new__创建'


def show_attr(cls):
    f = cls()
    if hasattr(cls, 'bar'):
        print(f'类({cls.__name__}), 小写属性:bar, 值为: {f.bar}')
    elif hasattr(cls, 'BAR'):
        print(f'类({cls.__name__}), 大写属性:BAR, 值为: {f.BAR}')
    else:
        print('未知异常.')


if __name__ == '__main__':
    print('----------判断当前类的属性大小写----------')
    show_attr(Foo)
    show_attr(FooOrigin)

    show_attr(FooTypeNew)
