"""
python3.5以上
"""
import asyncio


async def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        await asyncio.sleep(1)
        n -= 1


loop = asyncio.get_event_loop()  # 获取事件循环句柄
tasks = [  # 创建多个coroutine对象
    asyncio.ensure_future(countdown("A", 2)),
    asyncio.ensure_future(countdown("B", 3)),
    asyncio.ensure_future(countdown("c", 2)),
]
loop.run_until_complete(asyncio.wait(tasks))  # 循环运行
loop.close()
