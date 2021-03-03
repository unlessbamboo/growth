""" 守护线程测试 """
import time
import datetime
import threading


def show_time():
    """ 打印当前时间 """
    name = threading.current_thread().name

    # 在python主线程退出的时候会强制销毁
    while True:
        current_time = str(datetime.datetime.now())
        print('{}, 当前时间:{}'.format(name, current_time))
        time.sleep(1)


def count_down(n):
    name = threading.current_thread().name
    while n > 0:
        print('{}, 计数:{}'.format(name, n))
        time.sleep(0.5)
        n -= 1


if __name__ == '__main__':
    daemon_t = threading.Thread(target=show_time, name='daemon', daemon=True)
    daemon_t.start()

    c_t = threading.Thread(target=count_down, name='count', args=(10,))
    c_t.start()
    # 不需要等待守护线程
    c_t.join()
