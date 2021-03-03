# coding:utf8
"""
yield from 测试, 注意, yield from是 Python3.3 提出来的, 在python2.7中无法执行
"""


def return_ex():
    """ 测试yield from会返回其后生成器的 return 值 """
    yield 'return_yield_1'
    yield 'return_yield_2'
    yield 'return_yield_3'
    return 'return_return_4'


def show_return():
    value = yield from return_ex()
    print('生成器 1值:{}'.format(value))
    yield 'End'


if __name__ == '__main__':
    show = show_return()
    for v in show:
        print('生成器 2 返回:{}'.format(v))
