#!/usr/bin/env python

"""
@brief    merge sort simple test
      分析：
          1，本质上，一种比较类-非线性-归并类-分治思想-排序
          2，自顶向下-分治思想：
              步步为营，各个击破，大问题分解为若干小问题，最后组合。
              从一开始就自上而下，首先经过顶层，最后才到底层。
              空气干燥 --> 草原可能会发生大火 --> 各处的星星之火
          3，自底向上思想:
              虽然也是在一种大的约束下，但是推导时没有考虑合并后的操作，
              我们先干自己的，合并邻居，之后再说。
              星星之火，哪有志气和心情去燎原！

      附加：
          内排序：内存中的排序（归并、快排、堆排序、基数）
          外排序：
              核心：将文件分块放入内存，之后对内存中数据排序，写回文件
@author unlessbamboo
@version 1.0
@date 2016-02-15
"""


def merge(left, right):
    """merge:merge left and right. Notes, left and right
            are ordered list.

    :param left:
    :param right:
    """
    lindex, rindex = 0, 0
    left_len = len(left)
    right_len = len(right)
    result = []

    # 比较并将较小值放入新的列表中
    while lindex < left_len and rindex < right_len:
        if left[lindex] < right[rindex]:
            result.append(left[lindex])
            lindex += 1
        else:
            result.append(right[rindex])
            rindex += 1

    # 合并剩余的列表值
    result += left[lindex:]
    result += right[rindex:]

    return result


def mergeSortDC(list1, left, right):
    """mergeSortDC:自顶向下，采用递归方式，分治法思维：
            步骤：
                分解：将当前区间分解，分裂点(low+higth)/2下边界
                求解：递归的堆[low..mid]和[mid+1..high]进行归并排序
                组合：将上面已经排序的[low..mid]和[mid+1..high]进行merge操作
                PS:递归的终结条件为1

    :param list1:
    """
    if left >= right:
        return list1[left:right + 1]

    num = (left + right) / 2
    left_list = mergeSortDC(list1, left, num)
    right_list = mergeSortDC(list1, num + 1, right)

    return merge(left_list, right_list)


def mergePass(list1):
    """mergePass:自底向上归并处理
        1，子项长度：1, 2, 4, ..., n
        2，合并相邻的子项:
            [0..length]和[length..length + (length)]
            ...
            [i..length+i]和[length+i..length + (i+length)]
            (这里i的下标和数组下标保持一致，并且列表为左并右开)
        3，每次合并到最后，存在此类情况：
                存在奇数项,
                2*length > list_len and length < list_len
            此时必须将该奇数项加入到result中
            [i..length+i] 和 [length+i..list_len]

    :param list1:
    """
    list_len = len(list1)
    length = 1
    while length < list_len:
        i = 1
        result = []
        while i + 2 * length < list_len:
            result += merge(
                list1[i - 1:length + i - 1],
                list1[length + i - 1:length + length + i - 1])
            i = i + 2 * length

        # merge remain list
        if i + length - 1 < list_len:
            result += merge(
                list1[i - 1:length + i - 1],
                list1[length + i - 1:list_len])

        list1 = result
        length = length * 2

    return list1


def mergeKPass(list1, knum):
    """mergeKPass:多路自底向上归并处理
            分析：
                1，对单一数组进行拆分，其实多路归并排序一般
                    用于外部排序，此时文件都已经是一个个单一
                    的有序文件（快速排序等等措施进行小文件排序）
                2，读取k个值到内存中
                3，建立最大/最小堆结构，获取最小值，记录到output中
                4，重新读入新的值，重复步骤3

            案例：
                亿级整数个数的文件，如何进行排序输出？
                1，分解为有序文件，每一个文件可以是十万级别数组，进行
                    快速排序，产生有序文件；
                2，重复，直到读取所有的数据，这里进行了一次磁盘R/W操作

                3，对产生的M个临时文件进行k路归并排序，如果文件过多，
                    增加k值或者减小文件大小，步骤：
                    读取k个值，建立最小堆（调用heapsort中的create_heapify）；
                    写入最小值；
                    重新读取某一个队列中的值（该队列为最小值所在）；
                    重建最小堆（调用heapsort中的moveDown）；

            PS:
                上面的案例启示使用bit算法，不好，bit位在寻找特定值的
                应用场景中非常棒，步骤(假设40亿个数)：
                    1，人工设定位图中，最高位为1的数是value>20亿，最低位为1
                        的数是value<=20亿
                    2，读取大文件数据，并分别写入到两个文件中
                    3，继续上面的二分思维，直到最终找到最大值

    :param list1:
    :param knum:路数
    """
    pass


def displayList(list1):
    """displayList

    :param list1:
    """
    for value in list1:
        print value,
    print


if __name__ == '__main__':
    list1 = [25353, 535, 53, 5, 696, 2953, 502, 55, 332, 222]
    print '原始列表：'
    displayList(list1)
    # list1 = mergePass(list1)
    list1 = mergeSortDC(list1, 0, len(list1) - 1)
    print '排序后的列表：'
    displayList(list1)
    pass
