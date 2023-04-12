print(f"此时 __name__ 变量的值是：{repr(__name__)}")
print('执行顺序1: 顶层代码print')


def deco_bamboo(cls):
    """ 装饰器 """
    print('执行顺序: 装饰器函数定义体print')

    def inner(self):
        print('inner')

    cls.method_inner = inner
    return cls


class BambooClass:
    print('执行顺序2: 类定义体')

    def __init__(self):
        self.name = 'bamboo'

    class BambooInnerClass:
        print('执行顺序3: 内嵌类定义体')

    def show(self):
        print(f'show:{self.name}')
