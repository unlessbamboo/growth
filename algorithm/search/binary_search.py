# coding:utf8
"""
二分法查找和插值查找
"""

from __future__ import print_function


def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0

    while low < high:
        time += 1
        # 插值查找算法: low + int((high - low) * (key - lis[low])/(lis[high] - lis[low]))
        mid = int((low + high) / 2)
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印折半的次数
            print("对半查找的times: %s" % time)
            return mid

    return None


if __name__ == '__main__':
    src = [1, 5, 7, 8, 12, 16, 20, 22, 54, 99, 100, 123, 200, 222, 444]
    result = binary_search(src, 99)
    if result:
        print('下标:', result, ' 查找值:', src[result])
    else:
        print('查找失败')
