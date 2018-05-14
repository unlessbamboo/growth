#!/usr/bin/env python
# coding:utf-8


def A():
    try:
        print "xx"
        return
    except BaseException:
        print "err"
    else:
        print "---"
    return


if __name__ == '__main__':
    A()
