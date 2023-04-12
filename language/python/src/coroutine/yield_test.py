# coding:utf8
"""
python2下面, yield/send用法测试
"""


def iterator_yield(num):
    """ yield 组成的迭代器, 利用yield 不但返回 """
    value = num
    while value > 0:
        value = value - 1
        yield value
    # 返回空的时候for会自动处理异常
    return


def bamboo_generator():
    for _i in range(10):
        if _i == 5:
            return '中断循环, 返回'
        yield _i


def check_iterator_return():
    """ 验证yield的缺点, 在for语法糖中无法获取函数返回值 """
    print('------------test iterator return---------------')
    try:
        for item in bamboo_generator():
            print(item)
    except StopIteration as msg:
        print(msg)


def wrap_bamboo_generator(generator):
    """ 包装已有的生成器, 返回一个新的生成器 """
    result = yield from generator
    print(f'被包装生成器结果:{result}')


def check_yield_from_return():
    """ 验证yield from修复yield 无法返回return的问题 """
    print('------------test yield from return---------------')
    try:
        for item in wrap_bamboo_generator(bamboo_generator()):
            print(item)
    except StopIteration as msg:
        print(msg)


if __name__ == '__main__':
    # 1. 测试yield组成的迭代器
    for i in iterator_yield(5):
        print(i)
    # 2. 利用next
    it = iterator_yield(3)
    print('测试next:{}'.format(next(it)))

    # 3. 测试
    check_iterator_return()

    # 4. yield from test
    check_yield_from_return()
