""" 高阶函数实例

1. 函数式编程: 函数式一等对象
    + 对象在运行时创建
    + 对象可以赋值给变量或者作为数据结构元素, 可以作为参数传递
    + 对象可以作为返回值

2. 高阶函数: 
    + 接收函数作为参数;
    + 将函数作为返回值;

参考: https://developer.aliyun.com/article/749422
"""


def test_map():
    """ 测试map(func, dataList), 对dataList中的每一个元素调用func, 将函数返回值作为新的元素构建新的列表 

    @import: 回调函数返回值作为新数组的元素
    """
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = list(map(lambda x: x * x, l1))
    print(f'原始列表: {l1}, 最终列表: {l2}')

    # 2. 对字典中的整型加1
    d1 = {'name': 'bifeng', 'age': 18, 'salary': 50}
    d2 = dict(map(lambda kv: (kv[0], kv[1] + 1 if isinstance(kv[1], int) else kv[1]), d1.items()))
    print(f'原始字典: {d1}, 最终字典: {d2}')


def test_filter():
    """ 测试filter(func, datalist), 对datalist中的每一个元素调用func, 根据函数执行结果判断是否丢弃该元素

    @import: 回调函数返回值的boolean作为判断条件, 决定元素是否放入新数组
    """
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = list(filter(lambda x: x % 2 == 0, l1))
    print(f'原始列表: {l1}, 最终列表: {l2}')


def test_reduce():
    """ 测试reduce(func, datalit), 对datalist进行func(func(x1, x2), x3)的计算, 类似累加聚合

    @import: 注意, 其返回一个值而非列表
    """
    from functools import reduce
    l1 = [1, 2, 3, 4, 5, 6]
    value = reduce(lambda x, y: x + y, l1)
    print(f'原始列表: {l1}, 最终reduce值: {value}')


def test_sorted():
    """ 测试sorted(datalist, key=func, reverse=False), 对datalist进行排序, 
        每两个元素调用func, 返回排序后列表

    @import: 这是一个排序函数, 注意, func仅仅接收一个参数
    @import: python3中已经取消sorted中的cmp函数
    """
    l1 = [1, 19, 3, 90, 32, 6]
    l2 = sorted(l1, key=lambda x: x)
    print(f'通过key比较, 原始列表: {l1}, 最终列表: {l2}')

    from functools import cmp_to_key
    l3 = sorted(l1, key=cmp_to_key(lambda x, y: x > y))
    print(f'通过functools.cmp_to_key比较两个元素, 原始列表: {l1}, 最终列表: {l3}')


if __name__ == '__main__':
    print('-------测试map-------')
    test_map()
    print()

    print('-------测试filter-------')
    test_filter()
    print()

    print('-------测试reduce-------')
    test_reduce()
    print()

    print('-------测试sorted-------')
    test_sorted()
    print()
