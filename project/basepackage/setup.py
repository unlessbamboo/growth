""" basepackage包 """
import re
import sys
import os
import stat
import shutil
from setuptools import setup, find_packages

DATADIR = "/data/job"
LOGDIR = "/data/logs/job"
CONFDIR = "/data/conf/job"


def init_conf_env():
    """Initialize configure and modidy basepackage.ini"""
    # data
    conf = 'conf/basepackage.ini'
    with open(conf, 'r') as f:
        oldStr = f.read()
    with open(conf, 'w') as f:
        f.write(re.sub(f'\ndata=.*?\n', '\ndata={DATADIR}\n', oldStr))

    # logs
    conf = 'conf/basepackage.ini'
    with open(conf, 'r') as f:
        oldStr = f.read()
    with open(conf, 'w') as f:
        f.write(re.sub('\nlogs=.*?\n', f'\nlogs={LOGDIR}\n', oldStr))

    # baseconfig
    conf = 'basepackage/baseconfig.py'
    with open(conf, 'r') as f:
        oldStr = f.read()
    with open(conf, 'w') as f:
        f.write(re.sub(
            '\nCONF_DIR.*basepackage.ini\"?\n',
            f'\nCONF_DIR = "{CONFDIR}/basepackage.ini"\n', oldStr))


def create_directory():
    """Test data and log directory and make"""
    # data
    if not os.path.isdir(CONFDIR):
        os.makedirs(CONFDIR)

    # modify file authority
    try:
        os.chmod(CONFDIR, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    except Exception as msg:
        sys.stderr.write(f'User does not have modify permissions, msg:{msg}\n')


def copy_conf_file():
    """Copy configure file"""
    # basepackage
    conf = 'conf/basepackage.ini'
    if not os.path.exists(conf):
        sys.stderr.write(f'Note exists configure {conf}.\n')
        sys.exit(-1)
    shutil.copy(conf, CONFDIR + '/')

    # kafka
    conf = 'conf/kafka.ini'
    if not os.path.exists(conf):
        sys.stderr.write(f'Note exists configure {conf}.\n')
        sys.exit(-1)
    shutil.copy(conf, CONFDIR + '/')


def main():
    """main"""
    try:
        init_conf_env()
        create_directory()
        copy_conf_file()
    except Exception as msg:
        sys.stderr.write(f'Occur error, msg:{msg}.\n')
        sys.exit(-1)


main()

setup(
    name='basepackage',
    version='0.1',

    packages=find_packages(),
    # 依赖包名列表
    install_requires=['kafka'],
    # 元数据信息: 显示包的用途
    classifiers = [
    ]
    # 命令行工具: scripts参数(指定详细相对地址), console_script入口
    scripts = [],
    package_data={
        'basepackage': ['conf/*.ini'],
    },

    include_package_data=True,

    # exclude_package_data={},

    author='unlessbamboo',
    author_email='unlessbamboo@gmail.com',
    description='This is job\'s base packages.',
    license='JOB',
)
