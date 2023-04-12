""" 测试类装饰器
引申: 惰性取值装饰器, 见lazy_test.py

注意1: 通过归档带参数的函数装饰器和带参数的类装饰器, 一旦装饰器携带参数就必须在外层加一个包装, 多了一层
"""


class MyClassDecorator:
    def __init__(self, func):
        """ 类装饰器的统一逻辑: 在构造函数中接收装饰的实例对象: 函数, 类等 """
        self.func = func

    def __call__(self, *args, **kwargs):
        print('--------begin---------')
        result = self.func(*args, **kwargs)
        print('--------end---------')
        return result


class MyClassParams:
    """ 带参数的类装饰器: 整个逻辑和不带参数的类装饰器有很大的区别
    @common: __init__, __call__都是必须的
    """
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        def inner(*args, **kwargs):
            print('--------begin--------')
            print(f'类装饰器参数: {self.args}, {self.kwargs}')
            result = func(*args, **kwargs)
            print('--------end--------')
            return result
        return inner


@MyClassDecorator
def show_fullname(firstname, lastname):
    print(f'{firstname}-{lastname}')


@MyClassParams('参数1', age='kwargs参数')
def show_fullname_params(firstname, lastname):
    print(f'{firstname}-{lastname}')


def origin_show_fullname(firstname, lastname):
    print(f'{firstname}-{lastname}')
    return True


def parse_decorator(*args, **kwargs):
    """ 解析上面的装饰器, 上面的装饰器就可以拆解为如下的结构 """
    decoratorObj = MyClassDecorator(origin_show_fullname)
    # 因为类实现了__call__, 所以可以类似函数那样进行调用
    return decoratorObj(*args, **kwargs) 


def parse_decorator_params(*args, **kwargs):
    decoratorObj = MyClassParams('参数1', age='kwargs参数')
    func1 = decoratorObj(origin_show_fullname) 
    return func1(*args, **kwargs)


if __name__ == '__main__':
    print(f'1. 正常装饰测试:')
    show_fullname('zheng', 'bifeng')
    print()

    print(f'2. 拆解装饰测试:')
    parse_decorator('zheng', 'bifeng')
    print()

    print(f'3. 带参数类装饰测试:')
    show_fullname_params('zheng', 'bifeng')
    print()

    print(f'4. 带参数类拆解装饰测试:')
    parse_decorator_params('zheng', 'bifeng')
    print()
