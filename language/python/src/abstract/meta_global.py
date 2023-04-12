# coding:utf8
"""
使用__metaclass__属性来自定义类的创建流程
"""


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    # 1. 选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in list(future_class_attr.items()) if not name.startswith('__'))
    # 2. 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    # 3. 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


#  这会作用到这个模块中的所有类(仅仅适用于2.6)
__metaclass__ = upper_attr


class Foo(object, metaclass=upper_attr):
    """Foo:即Foo类创建时自动调用upper_attr来创建类"""
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
