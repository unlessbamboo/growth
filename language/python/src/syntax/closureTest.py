""" 作用于和闭包测试 """

def make_inc(x):
    """
    python闭包形成条件(javascript也是相同条件): 
        1. 内部函数嵌套
        2. 内部函数引用外部函数变量
        3. 内部函数被调用, 一般返回内部函数, 然后在外部被调用.
    闭包优点: 
        1. 延长外部函数变量生命周期(可能造成内存泄漏)
        2. 外部可以使用函数内部变量信息
    """
    z = 3
    print("ID(x):{0}, ID(z):{1}".format(id(x), id(z)))

    def inc(y):
        # 在函数inc中，x是闭合的，并关联
        return x + y, "Closure(z):id(z)-", id(z)
    # 返回动态的inc函数
    return inc


def show_inc():
    # 获取动态函数实例1
    inc5 = make_inc(5)
    # 获取动态函数的对象实例2
    inc10 = make_inc(10)

    # 打印__closure__中的值，预测值为：
    #   z的id是一样的，都引用了同一块内存值（作用域变为global，可以通过co_globals查看）
    #
    print("Inc5:")
    print("Value:", inc5.__closure__[0].cell_contents, "  ", inc5.__closure__[1].cell_contents)
    print("Id:", id(inc5.__closure__[0].cell_contents), "  ", id(inc5.__closure__[1].cell_contents))
    print("Inc10:")
    print("Value:", inc10.__closure__[0].cell_contents, "  ", inc10.__closure__[1].cell_contents)
    print("Id:", id(inc10.__closure__[0].cell_contents), "  ", id(inc10.__closure__[1].cell_contents))
