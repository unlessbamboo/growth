""" 多进程共享数据改动 """
import multiprocessing


# 测试1: 使用全局变量+锁来测试共享变量
global_x = 0


def main(obj):
    obj.value += 1
    # 问题: 不管如何改变, 都是在子进程中的全局变量进行变动, 对于进程的理解需要加深
    global global_x
    global_x += 1


if __name__ == '__main__':
    # 测试2: 使用multiprocessing中的共享value来测试共享变量, 其中'd'表示数据类型
    obj = multiprocessing.Value('d', 10.0)
    jobs = [multiprocessing.Process(target=main, args=(obj,)) for i in range(5)]
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()
    print('---' * 5)
    print(f'1. 最终进程池共享变量结果:{global_x}')
    print(f'2. 最终进程池共享变量结果:{obj.value}')
    print('---' * 5)
