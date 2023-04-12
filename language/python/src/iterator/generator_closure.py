""" 测试闭包在列表表达式和生成器表达式中的区别 """


def show_list():
    """ 列表表达式会实时进行计算, 但因为闭包的原因, 最终lambda中的i都是3 """
    def multiply():
        return [lambda x: i * x for i in range(4)]

    print('列表表达式: ', [m(100) for m in multiply()])


def show_generator():
    """ 生成器使用yield, 只有用到的时候才会组装lambda函数, 调用的时候i的值都是实时的 """
    def multiply():
        return (lambda x: i * x for i in range(4))

    print('生成器表达式: ', [m(100) for m in multiply()])


def show_normal_iter():
    def myrange():
        for i in range(4):
            yield lambda x: i * x

    def myrange2():

        for i in range(4):
            lambda x: i * x

    print('自定义生成器表达式: ', [m(100) for m in myrange()])


if __name__ == '__main__':
    print('---------测试闭包----------')
    show_list()
    show_generator()
    show_normal_iter()
    print()
