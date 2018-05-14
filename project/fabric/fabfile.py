# coding:utf8
"""
列出所有命令以及文档介绍:
    fab -f fabfile.py --list
"""
from fabric.api import local, lcd, run, env, cd, roles, settings, with_settings, hosts, parallel, hide
from fabric.api import output, task, abort, prefix, path, quiet, remote_tunnel
from fabric.contrib.console import confirm


# 运行环境设置, 见http://fabric-chs.readthedocs.io/zh_CN/chs/usage/env.html
# 类: env-字典的子类
# 功能: 设置, 任务间数据空间共享
# a)全局主机列表
#  env.hosts = ['160.14.183.193']
# b)建立ssh连接时的本地用户名
#  env.user = 'bamboo'
# c)建立ssh连接时需要提供的密码
#  env.password = 'bamboo'

env.roledefs = {
    'vps': ['root@65.49.195.86:29139'],
    'bamboo': ['bamboo@106.14.183.193'],
    'feng': ['ubuntu@150.109.43.228'],
}
env.use_ssh_config = True


def hello():
    """本地最基本的测试"""
    print('Hello world')


def helloargs(name, value):
    """测试传参"""
    print('{} = {}'.format(name, value))


def lsfab():
    """执行本地操作"""
    # 上下文管理器: lcd, 用于更新控制本地的目录
    with hide('running'):
        with lcd('./test1'):
            local('echo "使用lcd+with之后, 当前目录:"')
            local('pwd')
        local('echo ""')
        local('echo "仅仅使用lcd之后, 当前目录:"')
        local('pwd')


def addpath():
    """添加PATH"""
    # 上下文管理器: path
    with path('/data/', 'prepend'):
        local('echo $PATH')


def lslfab():
    """利用远程命令来连接本机, 默认使用当前用户"""
    with cd('./test1'):
        run('ls')


# 利用with_settings, 仅仅用于更改环境变量, 无法像上下文环境一样, 进行其他改动
@with_settings(lcd='~/grocery-shop')
def bamboomaster(message=None):
    #  with lcd('~/grocery-shop'):
    with settings(warn_only=True):
        local('pwd')
        local('git pull origin master')
        local('pwd')
        local('git add .')
        local('git commit -m "Auto commit by script"' if not message else 'git commit -m "{}"'.format(message))
        local('git push origin master')


# 装饰器: 指定相关条件, http://fabric-chs.readthedocs.io/zh_CN/chs/api/core/decorators.html
@roles('bamboo')
def bamboo():
    """用以替代shell"""
    # 上下文管理器迭代语法: with, 支持嵌套和&操作
    # 见https://www.rddoc.com/doc/Fabric/1.13.1/zh/api/core/context_managers/
    # 远程命令
    with cd('~/workspace/blog'):
        # 上下文管理器: prefix
        # 所有命令前缀: prefixCommand && childCommand
        with prefix('export BAMBOO=/root'):
            run('echo $BAMBOO')
            run('pwd')
            run('git pull origin master')
    # 用以检查当前目录
    run('pwd')
    # 切换工作目录, 但是可能在未来删除, 不建议
    with settings(cwd='~/workspace/blog'):
        run('pwd')


@roles('feng')
def feng():
    # 测试warn_only, 使用临时修改env会话管理器
    # 上下文管理器settings, 嵌套其他上下文管理器, 覆盖env变量
    with settings(warn_only=True):
        result = run('name -a')
    # 检查返回值, 并提供confirm功能, 简单的是/否提示
    if result.failed and not confirm('Test failed. Continue anyway?'):
        # 如果填写N, 执行该代码
        abort('执行失败')


@hosts(env.roledefs.get('vps')[0], env.roledefs.get('bamboo')[0])
def testhost():
    """测试hosts装饰器, 串行在所有host上执行, 可以通过env.hosts创建全局的hosts值
        默认情况下: 
            先执行主机1的所有任何;
            执行主机2
            ...
    """
    run('uname -a')
    run('echo "xxxxxxxxxxx:" `whoami`')
    run('echo "=========================="')


@hosts(env.roledefs.get('vps')[0], env.roledefs.get('bamboo')[0])
@parallel(pool_size=10)
def testparallel():
    """测试并行, 所谓的并行是所有主机通知执行下面的命令, 而并非在一台主机上并行执行命令, 没有这种需求的
        @Note: 输出是行级, 可能无法看出并行输出的结构, 最好看最开头的两条run命令
    """
    run('echo "xxxxxxxxxxx:" `whoami`')
    run('uname -a')
    run('ls /')
    run('echo "=========================="')


@hosts(env.roledefs.get('vps')[0], env.roledefs.get('bamboo')[0])
@parallel(pool_size=10)
def testoutput():
    """测试输出控制, 仅仅对输入信息/返回的输出信息进行控制, 不会影响实际服务器运行的打印级别
    """
    # 上下文管理器: hide, 隐藏running命令的调试信息, 例外还有stdout, stderr
    # 详细的输出级别见http://fabric-chs.readthedocs.io/zh_CN/chs/usage/output_controls.html
    with hide('stderr'):
        run('uname -a')
        run('echo "xxxxxxxxxxx:" `whoami`')
        run('echo "=========================="')


@roles('bamboo')
def testquiet():
    """安静模式下的命令执行"""
    # 上下文管理器quiet, 等价于settings(hide('everything'), warn_only=True)
    local('echo "xxxxxxxxxxxxxxxxxxxx"')
    with quiet():
        run('uname -a')
        run('echo "xxxxxxxxxxx:" `whoami`')
        run('echo "=========================="')


@roles('bamboo')
def testremotetunnel():
    """创建隧道, 让远程服务器连接本地服务"""
    with remote_tunnel(6379):
        run('redis-cli')
        run('echo "xxxxxxxxxxEnd Redisxxxxxxxxx"')
