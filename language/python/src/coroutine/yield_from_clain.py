"""
yield from 作为一个双向通道, 成功实现平均值求取
"""
import json
from collections import namedtuple


Result = namedtuple('Result', 'count average')


def averager():
    """ 子生成器: 求取平均值, 根据send过来的值不断进行累加并返回平均值 """
    print('Go into average generator...')
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
    在averager最终return之后才会返回表达式本身的值, 其他使用作为一个数据传输管道
    """
    results[key] = yield from averager()
    print('---Grouper结束运行---')
    return '委托end'


def main(_data):
    """ 统计平均值入口函数 """
    results = {}
    for key, values in _data.items():
        try:
            group = grouper(results, key)
            next(group)  # a. 初始化生成器(此时就开始进入子生成器), 注意, 这里相当于send(None)
            for value in values:  # b. 进行数据交互, 第一个send就开始进入average
                group.send(value)  # 'test'
            group.send(None)  # c. 将子生成器退出
        except Exception as msg:
            print(F'委托生成器最终的返回值:{msg}')
        finally:
            print('\n')
    # 虽然程序最后结束了, 但是grouper以及averager生成器并没有结束.
    print(f'最终的输入结果:\n{json.dumps(results, indent=2)}')


if __name__ == '__main__':
    data = {
        'girls;kg': [
            40.9,
            38.5,
            44.3,
            42.2,
            45.2,
            41.7,
            44.5,
            38.0,
            40.6,
            44.5],
        'girls;m': [
            1.6,
            1.51,
            1.4,
            1.3,
            1.41,
            1.39,
            1.33,
            1.46,
            1.45,
            1.43],
    }
    main(data)
