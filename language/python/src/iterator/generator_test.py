"""
功能: 生成器是迭代器的语法升级版本, 其实现一个自定义的迭代方式，而不是通过__iter__和__next__来进行构造

注意事项: 
    a. 使用yields语法时，返回的并不是一个iterator对象
    b. 不能使用next(obj)语法, 如果要使用，需要使用iter进行封装：
        iobj = iter(obj)
        next(iobj)
"""


def fib(num):
    """ 斐波那契, 对比iter_test.py中的Fib类, 对比生成器和迭代器的区别 """
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    print('----------斐波那契数列---------')
    print('结果: ', end='')
    for value in fib(10):
        print(value, end=' ')
    print()
