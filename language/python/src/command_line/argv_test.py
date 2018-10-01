# coding:utf8

import sys


def testSys():
    """testSys"""
    for arg in sys.argv[1:]:
        print(arg)


if __name__ == '__main__':
    testSys()
