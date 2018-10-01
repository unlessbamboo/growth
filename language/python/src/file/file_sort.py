# coding:utf8
"""
"""
import os
import stat


def sortdir(path, sort_cond='mtime', sort_filter=None,
            reverse=True, abspath=True, onlyfn=True, postfix=None):
    """
    sort dir by give condition & filter

    : param path: dir path
    : param sort_cond:
        ctime: create time
        mtime: last modify time
        atime: atime
        size: file size
    : param sort_filter:
        function to filter
        1: only file
        2: only dir
        3: both file and dir
        func: custom function
    : param reverse:
        if sort reversed
    : param abspath:
        if True, return list with absolute path of file
        or else, return relative
    : param onlyfn:
        if True, return [filename1, filename2, ....] at sort_cond
        else, return [(filename, os.stat(file), (), ...] at sort_cond

    : return:
        [(filename, os.stat(file), (), ...] at sort_cond
    """

    # sort condition
    sorts = {
        'mtime': lambda e: e[1].st_mtime,
        'ctime': lambda e: e[1].st_ctime,
        'atime': lambda e: e[1].st_atime,
        'size': lambda e: e[1].st_size,
    }
    f_sort_cond = sorts.get(sort_cond, sorts.get('mtime'))

    # sort filter
    f_sf = None
    if sort_filter is None or sort_filter is 3:
        # None, file or directory
        f_sf = None
    elif isinstance(sort_filter, type(lambda x: x)):
        # user defined function
        f_sf = sort_filter
    else:
        if sort_filter is 1:
            def f_sf(e):
                return stat.S_ISDIR(e.st_mode) is 0
        elif sort_filter is 2:
            def f_sf(e):
                return stat.S_ISDIR(e.st_mode)
        else:
            f_sf = None

    if onlyfn:
        # if onlyfn is True, return [filename1, filename2, ...]
        return [e[0] for e in _sortdir(path, f_sort_cond, f_sf, reverse, abspath, postfix)]
    else:
        return _sortdir(path, f_sort_cond, f_sf, reverse, abspath, postfix)


def _sortdir(path, sort_cond, sort_filter, reverse, abspath, postfix):
    """_sortdir: 对路径进行各种过滤处理, 最后根据key进行排序操作

    :param path: 待排序目录
    :param sort_cond: 比较函数, 用以判断
    :param sort_filter: 过滤指定格式的文件
    :param reverse:
    :param abspath: 是否为绝对路径
    :param postfix: 判断是否为指定postfix
    """
    fns = os.listdir(path)
    if not path.endswith('/'):
        path = path + '/'

    # Map: 对每一个item进行tranform, 对所有的文件进行路径拼装
    a_fns = [path + f for f in fns]
    # 获取所有文件的当前状况, 以列表格式返回
    sts = list(map(os.stat, a_fns))
    # Zip: 对各个参数进行zip打包操作, 以键值对(file, stat)作为元素存在
    res = list(zip(a_fns, sts)) if abspath else list(zip(fns, sts))

    n_res = []
    for e in res:
        if sort_filter and postfix:
            if postfix(e[0]) and sort_filter(e[1]):
                n_res.append(e)
        elif sort_filter and not postfix:
            if sort_filter(e[1]):
                n_res.append(e)
        elif not sort_filter and postfix:
            if postfix(e[0]):
                n_res.append(e)

    # sorted:
    #   key--获取迭代器中的一个元素并调用相应函数
    #   cmp--获取迭代器中的多个元素并调用相应函数
    return sorted(n_res, key=sort_cond, reverse=reverse)


def remove_outdate_files(file_list, file_number):
    """
    remove outdate filenames
    """
    list_length = len(file_list)
    print(list_length)
    if file_number > list_length:
        return

    for index in range(file_number - 1, list_length):
        os.remove(file_list[index])
        print(file_list[index])
    print('Remove outdate files end')


if __name__ == '__main__':
    """
    Main
    """
    file_list = sortdir('/home/temp/', postfix=lambda f: f.endswith('.info'))
    for element in file_list:
        print(element)
    remove_outdate_files(file_list, 20)
