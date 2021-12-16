""" 作用于和闭包测试
note1: Python 不像javascript, 没有变量提升操作
"""


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
    print(f"ID(x):{id(x)}, ID(z):{id(z)}")

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


def show_scope():
    """ 展示函数作用域
    1. 类似javascript, 在代码预解析阶段就已经决定了作用域信息, 后续闭包回调函数不管在哪里调用,
        其作用域链都是不变的
    """
    name = 'global scope'

    def show_inner_scope():
        name = 'inner scope'

        def show_current_scope():
            print(f'当前变量:{name}')

        return show_current_scope

    func = show_inner_scope()
    func()  # 输出: inner scope


if __name__ == '__main__':
    # 1. 测试闭包作用域信息
    show_inc()

    # 2. 测试
    show_scope()
