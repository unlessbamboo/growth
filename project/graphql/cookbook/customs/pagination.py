"""
    pagination.py
"""
from django.core.paginator import Paginator, EmptyPage


class XPaginator(object):
    """
    Example:
        XPaginator(objs, page).map(function_cb)
    """
    def __init__(self, objs, page=0, page_size=10):
        try:
            self.paginator = Paginator(objs, page_size)
            self.page_objs = self.paginator.page(page)
        except EmptyPage:
            self.page_objs = self.paginator.page(self.paginator.num_pages)

    def result(self, data):
        return {
            'data': data,
            'count': self.paginator.count,
            'page': self.page_objs.number,
            'pages': self.paginator.num_pages,
            'page_size': self.paginator.per_page,
        }

    def map(self, cb):
        """根据回调地址进行分页map操作"""
        data = []
        for obj in self.page_objs:
            r = cb(obj)
            if r:
                data.append(r)

        return {
            'data': data,
            'count': self.paginator.count,
            'page': self.page_objs.number,
            'pages': self.paginator.num_pages,
            'page_size': self.paginator.per_page,
        }


def x_paginator_objs(objs, page=0, page_size=10):
    try:
        paginator = Paginator(objs, page_size)
        page_objs = paginator.page(page)
    except EmptyPage:
        page_objs = paginator.page(paginator.num_pages)
    return page_objs
