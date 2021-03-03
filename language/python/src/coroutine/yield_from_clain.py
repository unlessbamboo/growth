"""
yield from 作为一个双向通道, 成功实现平均值求取
"""
import json
from collections import namedtuple


Result = namedtuple('Result', 'count average')


def averager():
    """ 求取平均值, 根据send过来的值不断进行累加并返回平均值 """
    count = total = 0.0
    while True:
        term = yield 'test'  # 这里'test'仅仅作为测试使用
        if term is None:
            break
        total += term
        count += 1
    return Result(count, total / count)


def grouper(results, key):
    """ 双管道, 会自动将main中send的值传递给averager,
    在averager最终return之后才会返回表达式本身的值.
    """
    while True:
        results[key] = yield from averager()
    print('---Grouper结束运行---')


def main(data):
    """ 统计平均值入口函数 """
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        # 实际上类似初始化, 会在averager的yield处停住. 
        # next返回averager中抛出的'test'值, 这里没用
        next(group)
        for value in values:
            group.send(value)  # 这个语句本身会返回'test'
        group.send(None)  # 结束
    # 虽然程序最后结束了, 但是grouper以及averager生成器并没有结束.
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    data = {
        'girls;kg':[40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
        'girls;m':[1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    }
    main(data)
