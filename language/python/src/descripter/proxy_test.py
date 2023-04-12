""" 描述符的代理类使用方法, 具体见descripter_test.py文件 """


class CharacterDescriptor:
    """ 描述性格的专用类 """
    def __init__(self, key):
        self.key = key

    def __get__(self, instance, owner):
        """ instance表示类实例, owner表示类 """
        print(f'性格: get, instance: {instance}, owner: {owner}')
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise Exception('xxxxxx')
        instance.__dict__[self.key] = value


class NumDescriptor:
    def __init__(self, key):
        self.key = key

    def __get__(self, instance, owner):
        print('Number get')
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise Exception('xxxxxxx')
        instance.__dict__[self.key] = value


class Person:
    """ 描述符类似代理类 """
    # 必须把描述符定义成这个类的类属性，不能定义到构造函数中
    name = CharacterDescriptor('name')
    age = NumDescriptor('age')

    def __init__(self, name, age):
        # 此时相当于为对象的类属性赋值: cls.name = '碧锋', 此时会走setter流程
        self.name = name
        self.age = age

    def show(self):
        print(f'用户:{self.name}, 年龄: {self.age}')


if __name__ == '__main__':
    # 1. 传入正确的类型
    print('----------正确类型-----------')
    Person('bifeng', 18).show() 
    print()

    print('----------错误类型-----------')
    Person('bifeng', '18').show() 
    print()
