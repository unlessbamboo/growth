""" 同步锁操作 """
import time
import sys
import multiprocessing


stream = sys.stdout


def lock_with_worker(lock):
    """ 进程锁写数据 """
    name = multiprocessing.current_process().name
    for _ in range(3):
        with lock:
            stream.write('proces:{} ready write message\r\n'.format(name))
            stream.flush()
        time.sleep(0.5)


def lock_nowith_worker(lock):
    """ 进程2写数据 """
    name = multiprocessing.current_process().name
    for _ in range(3):
        lock.acquire()
        try:
            stream.write('process:{} du du du du\r\n'.format(name))
            stream.flush()
        finally:
            lock.release()  # 释放锁
            time.sleep(0.3)


if __name__ == '__main__':
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(name='with', target=lock_with_worker, args=(lock,))
    p2 = multiprocessing.Process(name='nowith', target=lock_nowith_worker, args=(lock,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
