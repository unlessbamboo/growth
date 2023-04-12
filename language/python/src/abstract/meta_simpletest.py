"""
功能: 实现和测试type相关的简单测试
"""


def create_empty_class():
    """ 使用type创建一个空的类并进行简单的测试 """
    MyClass = type('MyClass', (), {'name': '我是空值'})
    obj = MyClass()
    print('--------创建一个空类, 基类为空--------')
    print(f'类: {MyClass}, 对象: {obj}, 属性name的值: {obj.name}')
    try:
        MyClass(18, desc='无效参数')
    except Exception:
        print('--此时类不能传入参数进行实例化')
    print()
    return MyClass


def create_child_empty_class(ParentClass):
    """ 使用type创建的空类作为基类, 再次使用type创建新的类 """
    MyChildClass = type('MyChildClass', (ParentClass,), {'age': 18})
    obj = MyChildClass()
    print('--------创建一个空类, 基类为MyClass--------')
    print(f'类: {MyChildClass}, 对象: {obj}, 属性name(继承自父类)的值: {obj.name}, age值: {obj.age}')


if __name__ == '__main__':
    # 1. 空类, 此时类的实例化不能传值
    empty_class = create_empty_class()
    # 2. 空类的子类
    create_child_empty_class(empty_class)
