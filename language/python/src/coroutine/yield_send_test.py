# coding:utf8
"""
yield和send用法介绍
"""


def iterator_yield(maxnum):
    """ 传入一个最大值, 一旦迭代超过该值, 结束 """
    step = 0
    while step < maxnum:
        # 注意, 这里yield将结果step抛出, 之后会将外面通过send传入的结果传入jump中
        jump = yield step
        if jump is None:
            step += 1
        else:
            print('传入一个新的step值:{}'.format(jump))
            step = step + jump


if __name__ == '__main__':
    # 1. 迭代器测试
    it = iterator_yield(6)
    print(next(it))
    it.send(3)
    print(next(it))
