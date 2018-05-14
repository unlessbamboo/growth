# coding:utf8
"""
处于代码模块化的考虑, 使用'新式任务'来定义fab命令, 一旦在文档中定义了task,
并使用了task装饰器, 那么表示当前文档所有命令都会使用该方式, 老的定义命令方式将失效.
"""
from fabric.api import local, lcd, run, env, cd, roles, settings, with_settings, hosts, parallel, hide
from fabric.api import output, task


@task
def hello():
    """本地最基本的测试"""
    print('Hello world')


def hello1():
    """本地最基本的测试"""
    print('Hello world')


@task(alias='hello2')
def hello_world_bamboo():
    """使用别名进行命令定义"""
    print('Hello world.')


@task(default=True)
def welcome():
    """默认任务"""
    print('Welcome to fabric.')
