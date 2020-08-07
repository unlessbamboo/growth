import threading
import time


class B(object):
    def __init__(self):
        self.token = 0

    def parse(self, index, token, m):
        m.acquire()
        try:
            print('线程{} token:{} 锁:{}'.format(index, token, id(m)))
            time.sleep(0.5)
        finally:
            m.release()



mutex = threading.Lock()
threads = []
obj = B()
for i in range(5):
    t = threading.Thread(target=obj.parse, args=(i, i*10, mutex))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
