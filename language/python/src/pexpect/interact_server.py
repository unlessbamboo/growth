# coding:utf8
"""
测试在连接远端服务器之后, 调用interact让出控制权
"""
import sys
import pexpect


def interact_server():
    # 确保logfile不是stdout, 否则输入会有冗余数据
    child = pexpect.spawnu('mygo bamboo')
    child.expect(['~'])
    print('--------------------------')
    child.interact()
    print('--------------------------')

    # interact之后child就失效了
    child = pexpect.spawnu('mygo bamboo')
    child.logfile = sys.stdout
    print('--------------------------')
    child.expect(['.', pexpect.EOF])
    print('--------------------------')


if __name__ == '__main__':
    interact_server()
