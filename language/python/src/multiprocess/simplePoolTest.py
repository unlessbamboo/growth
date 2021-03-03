""" 进程池操作 """
import time
import sys
import multiprocessing


def start_func():
    name = multiprocessing.current_process().name
    print('进程池初始函数, 名字:{}.....'.format(name))


def show_myself(data):
    name = multiprocessing.current_process().name
    print('{}: {}'.format(name, data))


if __name__ == '__main__':
    # 1. 创建进程池
    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size, initializer=start_func, maxtasksperchild=2)
    
    # 2. 获取准备传入多个进程的各个数据
    input_datas = ['aa', '33', 'bb', 'dd', '想', '你妹', '哇哈', '30', 'omg']

    # 3. 迭代启动
    pool_outpus = pool.map(show_myself, input_datas)

    # 4. 关闭
    pool.close()
    pool.join()
