""" 多进程利用队列来进行传递消息 """
import time
import queue
import multiprocessing


def worker(q):
    """ 消费者 """
    name = multiprocessing.current_process().name
    for _ in range(3):
        try:
            message = q.get(timeout=2)
            if message:
                print('子进程{}收到消息:{}'.format(name, message))
        except queue.Empty:
            print('-----------子进程结束-------------')
            break


if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()

    # 生产者
    for i in range(3):
        q.put(i)
    # 等待消费者
    q.close()
    q.join_thread()
    p.join()
    print('==========================')
