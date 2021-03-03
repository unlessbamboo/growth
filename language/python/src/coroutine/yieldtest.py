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


if __name__ == '__main__':
    # 1. 测试yield组成的迭代器
    for i in iterator_yield(5):
        print(i)
    # 2. 利用next
    it = iterator_yield(3)
    print('测试next:{}'.format(next(it)))
