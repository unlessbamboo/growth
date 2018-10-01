# coding:utf8
"""
使用MetaClass类来进行类的创建, 而不是使用metaclass属性.
注意:
    'type'实际上是一个类，就像'str'和'int'一样, 所以，你可以从type继承.

    __new__ 是在__init__之前被调用的特殊方法, 是用来创建对象并返回之的方法;
    __init__只是用来将传入的参数初始化给对象;
"""


class UpperAttrMetaClass(type):
    """UpperAttrMetaClass
    """
    def __new__(mcs, future_class_name, future_class_parents, future_class_attr):
        """__new__

        :param mcs: metaclass
        :param future_class_name: 类名
        :param future_class_parents: 父类
        :param future_class_attr: 属性
        """
        attrs = ((name, value) for name, value in list(future_class_attr.items()) if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type(future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass2(type):
    def __new__(mcs, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in list(future_class_attr.items()) if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        # 复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(mcs, future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass3(type):
    def __new__(mcs, name, bases, dct):
        attrs = ((name, value) for name, value in list(dct.items()) if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(mcs, name, bases, uppercase_attr)


class UpperAttrMetaclass4(type):
    def __new__(mcs, name, bases, dct):
        attrs = ((name, value) for name, value in list(dct.items()) if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass4, mcs).__new__(
            mcs, name, bases, uppercase_attr)


class Foo(object, metaclass=UpperAttrMetaClass):
    bar = 'bamboo'


if __name__ == '__main__':
    if hasattr(Foo, 'bar'):
        f = Foo()
        print('Lower:', f.bar)
    elif hasattr(Foo, 'BAR'):
        f = Foo()
        print('Upper:', f.BAR)
    else:
        print('XXXXXXXXXXX')
