""" 浅拷贝和深拷贝: 自定义深拷贝类

1. 深拷贝问题:
    a. 对象引用其自身的时候会发生无限递归, 此时可以通过memo字典记录已经复制的值来避免递归
    b. 对于一些共享数据对象, 在深拷贝的时候会产生多份数据

2. 列表切片实际上就是相当于浅拷贝

注意: 魔术方法就是python中的一种约定, 多个相关的约定组合成一种协议, 通过协议来实现一些特殊的功能
"""
import copy
import functools


@functools.total_ordering
class CopyClass:
    def __init__(self, name, info):
        self.name = name
        self.info = info  # 列表

    def __eq__(self, other):
        return self.name == other.name and self.info == other.info

    def __gt__(self, other):
        return self.name > other.name

    def __copy__(self):
        """ 浅拷贝 """
        # 浅拷贝就是实例化一个新的对象
        return CopyClass(self.name, self.info)

    def __deepcopy__(self, memo):
        return CopyClass(copy.deepcopy(self.name, memo), copy.deepcopy(self.info, memo))

    def show(self):
        print(f'名称: {self.name}, 数据: {self.info}')


if __name__ == '__main__':
    obj = CopyClass('bifeng', ['sh', 'bj', 'tj'])
    print('----------浅拷贝----------')
    print('-原始数据: ')
    obj.show()
    print('-拷贝数据: ')
    nobj = copy.copy(obj)
    nobj.show()
    print()

    print('>> 对原始数据进行改动')
    obj.info.append('newYork')
    print('-原始数据: ')
    obj.show()
    print('-拷贝数据: ')
    nobj.show()
    print()

    print('----------深拷贝----------')
    print('-原始数据: ')
    obj.show()
    print('-拷贝数据: ')
    nobj = copy.deepcopy(obj, {})
    nobj.show()
    print()

    print('>> 对原始数据进行改动')
    obj.info.append('Paris')
    print('-原始数据: ')
    obj.show()
    print('-拷贝数据: ')
    nobj.show()
