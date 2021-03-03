"""
该代码建议在python3.4下运行
"""
import asyncio


@asyncio.coroutine
def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        # 在python3.5之前, 使用yield from代替await
        # 注意asyncio.sleep是专门用于异步编程的, 如果是time.sleep, 则会直接阻塞
        yield from asyncio.sleep(1)
        n -= 1


loop = asyncio.get_event_loop()  # 获取事件循环句柄
tasks = [  # 创建多个coroutine对象
    asyncio.ensure_future(countdown("A", 2)),
    asyncio.ensure_future(countdown("B", 3)),
    asyncio.ensure_future(countdown("c", 2)),
]
loop.run_until_complete(asyncio.wait(tasks))  # 循环运行
loop.close()
