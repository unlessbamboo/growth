# coding:utf8
"""
功能: 重命名当前目录下的所有文件, 将'-'转为'_', 使用os.walk进行自动递归遍历
"""
import os


def rename_all(path):
    """rename_all

    :param path: 待检索的目录
    """
    for rootpath, dirnames, filenames in os.walk(path):
        print 'Root:', rootpath
        for filename in filenames:
            new_filepath = rootpath + os.sep + filename.replace('-', '_')
            filepath = rootpath + os.sep + filename
            os.rename(filepath, new_filepath)

        for dirname in dirnames:
            new_dirpath = rootpath + os.sep + dirname.replace('-', '_')
            dirpath = rootpath + os.sep + dirname
            os.rename(dirpath, new_dirpath)


rename_all('.')
