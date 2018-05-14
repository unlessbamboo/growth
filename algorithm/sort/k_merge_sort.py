# coding:utf8
"""
多路归并排序
"""

import heapq


def kmerge(iterables, keyFcn=None):
    _heappop, _heapreplace, _StopIteration = heapq.heappop, heapq.heapreplace, StopIteration
    # 用于生成迭代器的函数
    _iter = iter

    h = []

    # 1 利用map函数式编程函数, 对iterables中所有列表进行转换, 返回一个生成器列表
    for itnum, it in enumerate(map(_iter, iterables)):
        try:
            next = it.next
            if keyFcn is not None:
                h.append([keyFcn(next()), itnum, next])
            else:
                h.append([next(), itnum, next])
        except _StopIteration:
            pass

    # 2 这里利用生成器来进行一次次进行归并排序, 此时h中存储了所有k路的所有
    #   首位记录
    heapq.heapify(h)

    while True:
        try:
            while True:
                v, itnum, next = s = h[0]   # raises IndexError when h is empty
                yield v

                if keyFcn is not None:
                    s[0] = keyFcn(next())
                else:
                    s[0] = next()       # raises StopIteration when exhausted
                _heapreplace(h, s)          # restore heap condition
        except _StopIteration:
            _heappop(h)                     # remove empty iterator
        except IndexError:
            return


if __name__ == '__main__':
    x = kmerge([
        [1, 3, 5, 7],
        [0, 2, 4, 8],
        [5, 10, 15, 20],
        [],
        [25]
    ])
    for i in x:
        print i,
    print
