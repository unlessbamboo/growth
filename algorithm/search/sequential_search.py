# coding:utf8
"""
无序表检索
"""

from __future__ import print_function


def sequential_search(lis, key):
    for i in range(len(lis)):
        if lis[i] == key:
            return i
    return None


if __name__ == '__main__':
    src = [1, 0, 123, 53, 293, 8, 123, 22, 54, 7, 92, 303, 222]
    index = sequential_search(src, 123)
    if index:
        print('下标:', index, ' 值:', src[index])
    else:
        print('未找到')
