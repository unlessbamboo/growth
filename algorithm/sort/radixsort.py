# coding:utf8

"""
@file radixsort.py
@brief    radix sort simple test
      分析：
          1，本质上，一种非比较类-线性时间-分配类-排序
          2，术语：
              分量-d：
                  所需进行桶排序的数量，每一次的基数都不一样的
              单关键字：
                  例如十进制整数，d的值为最长位数，每次的基数都是10
              多关键字：
                  例如扑克牌花色，d的值为花色取值、点数，每次的基数不一样
          3，算法过程：
              1）NB公司求职？好几个备胎人选？还有好几关面试？
              2）保证每一次的桶排序，大哥我都在优先队列
              3）此轮排序的基数都是在前一轮排序的基础上的，技术第一嘛，OK
          4，排序方式：
              LSD：低位优先排序
              MSD：高位优先排序
@author unlessbamboo
@version 1.0
@date 2016-02-16
"""
import math


def radixSort(list1, radix):
    """radixSort

    :param list1: 带排序数组
    :param radix: 基数, 需要提前设置
    """
    # 用K位数可表示任意整数
    # 1 首先根据radix基数(10进制, 15进制)来获取lnN的值: math.log(Max, radix)
    # 2 之后获取向上取整值: math.ceil(value)
    # 3 最后才得到桶的数量
    k = int(math.ceil(math.log(max(list1) + 1, radix)))
    for i in range(1, k + 1):
        # 设置某一位基数位时的桶
        bucket = [[] for j in range(radix)]
        for val in list1:
            bucket[val % (radix**i) // (radix**(i - 1))].append(val)
        del list1[:]

        # 桶合并
        for each in bucket:
            list1.extend(each)
    return list1


def displayList(list1):
    """displayList

    :param list1:
    """
    for value in list1:
        print value,
    print 'x'


if __name__ == '__main__':
    list1 = [25353, 535, 53, 5, 696, 2953, 502, 55, 332, 222]
    print '原始列表：'
    displayList(list1)
    list1 = radixSort(list1, 10)
    print '排序后的列表：'
    displayList(list1)
    pass
