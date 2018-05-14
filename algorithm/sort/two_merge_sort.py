# coding:utf8
"""
二路归并排序.

MergeSort(array, p, q)
    功能: 对数组进行排序, 采用分治, 二路归并排序

Merge(array, low, middle, high)
    条件:array前半部分是已经排序, 后半部分已经排序 
    功能: 将array的前半部分和后半部分进行二路归并排序, 分治法的归并收缩阶段
"""
from __future__ import print_function
import time  
import sys  


def Merge(array, low, middle, high):  
    # 左有序队列长度
    n1 = middle - low + 1
    # 右有序队列长度
    n2 = high - middle  
    left_array = []  
    right_array = []  

    # 把array 左边的值，放到left_arr  数组里面  
    left_array = [array[i + low] for i in range(0, n1)]
    # 把 array 右边的值，放到 right_arr  数组里面  
    right_array = [array[j + middle + 1] for j in range(0, n2)]

    i, j = 0, 0  
    k = low  
    while i != n1 and j != n2:  
        if left_array[i] <= right_array[j]:  
            array[k] = left_array[i]  
            k += 1  
            i += 1  
        else:  
            array[k] = right_array[j]  
            k += 1  
            j += 1  

    while i < n1:  
        array[k] = left_array[i]  
        k += 1  
        i += 1  

    while j < n2:  
        array[k] = right_array[j]  
        k += 1  
        j += 1  


def MergeSort(array, p, q):  
    """分治, 不断的分解, 再自下而上归并"""
    if p < q:
        # 转成int  类型  
        mid = int((p + q) / 2)  
        MergeSort(array, p, mid)  
        MergeSort(array, mid + 1, q)  
        Merge(array, p, mid, q)  


if __name__ == "__main__":  
    # mylist=[1,45,56,34,67,88,54,22]  
    mylist = [1, 34, 6, 21, 98, 31, 7, 4, 56, 59, 27, 13, 36, 47, 67, 37, 25, 2]  

    print('Origin: ', mylist)
    MergeSort(mylist, 0, len(mylist) - 1)  
    print('Result: ', mylist)  
