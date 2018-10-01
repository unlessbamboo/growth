# coding:utf-8
"""
文件递归查找和打印
"""
import os


def recursePath(path):
    """
    @rootpath: 整个path的起始根路径
    @dirnames：所有的目录项
    @filenames：所有的文件项

    功能: walk本身逐级遍历，一层层进入
    """
    for rootpath, dirnames, filenames in os.walk(path):
        print(rootpath + '/')
        for memo in dirnames:
            print(memo + '/')

        for memo in filenames:
            print(memo)


if __name__ == '__main__':
    """main"""
    recursePath('../webOperator')
