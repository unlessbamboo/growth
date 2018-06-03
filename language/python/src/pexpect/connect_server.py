# coding:utf8
"""
简单的测试pexpect功能, 并调用interact让出控制权
"""
import sys
import pexpect


def connect():
    child = pexpect.spawnu('mygo bamboo')
    # 指定标准输出或者文件
    child.logfile = sys.stdout

    child.expect([u'~'])
    print '--------------------------'
    child.sendline('ls -l')
    print '--------------------------'
    # 确保能够捕获, 否则一致等待
    child.expect([u'.*', pexpect.EOF])
    print '--------------------------'


if __name__ == '__main__':
    connect()
