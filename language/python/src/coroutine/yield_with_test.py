"""
功能: 在一个with语句中循环处理某一个代码
@output:
    Entry
    yield
    -----------------
    ...
    -----------------
    exit
    exit
    exit
    ...
"""
import time
from contextlib import contextmanager


G_NUMBER = 1


@contextmanager
def test():
    try:
        print('Entry')
        yield 'yield'
        time.sleep(0.5)
        print('---' * 5)
        raise
    except:
        global G_NUMBER
        G_NUMBER += 1
        if G_NUMBER <= 5:  # 递归循环
            with test() as t1:
                print(t1)
    finally:
        print('exit')


if __name__ == '__main__':
    with test() as t:
        print(t)
