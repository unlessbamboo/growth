#!/usr/bin/env python
# coding:utf-8
import logging


def A():
    try:
        print("xx")
        return
    except BaseException:
        print("err")
    else:
        print("---")
    return


if __name__ == '__main__':
    A()
