# coding:utf8
"""
切割大的日志文件为一个个的小文件
"""
import threading
import time
import os
import shutil
import re
import psutil


# 分割日志临时目录
TMP_DIR = '/data/logs/nginx_tmp/'
NGINX_LOG_DIR = '/data/logs/nginx/'


def init():
    """
    初始化所有为临时文件夹
    """
    # 分割日志临时目录
    if os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)
    if not os.path.exists(NGINX_LOG_DIR):
        raise Exception(
            'Not found nginx log directory:{}'.format(NGINX_LOG_DIR))


def split():
    """split: 切割日志"""
    # 此数字是按字节进行计算，这里大小为内存除以cpu核数剩以0.5得到的结果为500M
    cpu_count = psutil.cpu_count()
    memory_size = psutil.total
    sizehint = int(memory_size / cpu_count * 0.5 * 1024 * 1024)

    for nginx_log_file in os.listdir(NGINX_LOG_DIR):
        nginx_log_path = NGINX_LOG_DIR + nginx_log_file
        with open(nginx_log_path) as fp:
            position = 0
            file_num = 1
            while True:
                lines = fp.readlines(sizehint)
                # 分割成功的文件名
                split_file_name = TMP_DIR + \
                    os.path.splitext(nginx_log_file)[0] + '_' + file_num + '.log'
                with open(split_file_name, 'w') as split_fp:
                    split_fp.writelines(lines)
                if fp.tell() - position <= 0:
                    break
                # 如果分割的位置大于默认位置就继续执行，否则就退出。
                position = fp.tell()  # 替换位置
                file_num = file_num + 1
        #  os.remove(nginx_log_path)
        time.sleep(5)


if __name__ == '__main__':
    # 执行程序开始时间
    print('Start at:', int(time.strftime('%H%M%S')))
    split()
    print('Stop at:', int(time.strftime('%H%M%S')))
