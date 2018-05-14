# coding:utf8
from __future__ import print_function
import sys


def testSys():
    """testSys"""
    for arg in sys.argv[1:]:
        print(arg)


if __name__ == '__main__':
    testSys()
