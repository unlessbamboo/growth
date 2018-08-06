# coding:utf8
"""
定时写入数据到文件中
"""
import time


def test():
    index = 0
    while True:
        with open('/tmp/test.txt', 'a') as f:
            f.write('----------test({})------------\n'.format(index))
        index += 1
        time.sleep(3)


test()
