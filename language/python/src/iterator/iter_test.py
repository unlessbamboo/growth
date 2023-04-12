"""
功能: 实现了迭代器协议，真正实现底层操作，对比生成器方法, 该方式非常麻烦和复杂
条件: 
    a. 定义__iter__方法，返回本身（即返回一个定义了next方法的对象）
    b. 定义__next__方法或者next方法，返回下一个
"""


class Count:
    """ Count:从1数到10 """

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        """ 初始化时被调用: 返回自身
        @注意: 从这里就可以看出迭代器自身为何, 节省内存消耗，使用"懒惰属性"
        """
        print('>> __iter__被调用')
        self.start = 0
        return self

    def __next__(self):
        """ 每次遍历迭代器元素或者调用next方法的时候调用 """
        if self.start >= self.max:
            raise StopIteration  # with语法糖会自动处理该异常

        value = self.start
        self.start += 1
        return value


class Fib:
    """ 斐波那契数列迭代器 """

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()



if __name__ == '__main__':
    """main"""
    print('-----------迭代求和----------')
    count_num = 100000
    obj = Count(count_num)
    total_value = 0
    for num in obj:
        total_value += num
    print(f'{count_num}的求和结果为: {total_value}')
    print()

    print('----------斐波那契数列---------')
    print('结果: ', end='')
    for value in Fib(10):
        print(value, end=' ')
    print()
