""" 标记清除

标记阶段: 从根节点出发, 将所有可访问对象设置为"可达"
清除阶段: 将所有未标记的对象回收

参考: https://juejin.cn/post/7119018622906957854
"""


class A:
    pass


def myfunc() -> list:
    """ 测试标记清除.

    :rtype: list
    """
    a1, a2, a3, a4 = A(), A(), A(), A()

    # 1. 循环引用
    a1.obj, a2.obj = a2, a1

    return [a3, a4]


# 此时rootobj就是某一个根节点, 从该节点触发可到达: a3, a4内存空间, 此时这两个对象被标记为"可达", 而a1, a2
# 即使在函数调用完成之后未释放也会在后续的清理阶段被清除
rootobj = myfunc()
