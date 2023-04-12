"""
该代码建议在python3.4下运行
"""
import time
import asyncio


@asyncio.coroutine
def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        # 在python3.5之前, 使用yield from代替await
        # 注意asyncio.sleep是专门用于异步编程的, 如果是time.sleep, 则会直接阻塞
        _start = time.time()
        yield from asyncio.sleep(1)
        _end = time.time()
        print(f'{number} --> {round(_end - _start, 3)}')
        n -= 1


loop = asyncio.get_event_loop()  # 获取事件循环句柄
start = time.time()
tasks = [  # 创建多个coroutine对象
    asyncio.ensure_future(countdown("A", 2)),
    asyncio.ensure_future(countdown("B", 3)),
    asyncio.ensure_future(countdown("c", 2)),
    asyncio.ensure_future(countdown("d", 0)),
    asyncio.ensure_future(countdown("e", 5)),
    asyncio.ensure_future(countdown("f", 2)),
]
loop.run_until_complete(asyncio.wait(tasks))  # 循环运行
loop.close()
end = time.time()
""" 输出说明:
1. 串行执行预期耗时:
    2 + 3 + 2 + 0 + 5 + 2 == 14
2. 实际耗时:
    max(2, 3, 2, 0, 5, 2) == 5
所以协程并发缺失达到预期的目标, 将IO和CPU执行区分开来.
"""
print(f'整个过程总耗时:{int(end - start)}')
