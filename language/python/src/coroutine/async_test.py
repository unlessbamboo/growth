import asyncio


async def sleepN(num):
    for _ in range(10):
        await asyncio.sleep(1)
        print('IO结束, 回调开始======:{}'.format(num))

    return 'End:{}'.format(num)

tasks = []
for i in range(20):
    tasks.append(asyncio.ensure_future(sleepN(i)))

loop = asyncio.get_event_loop()  # 获取事件循环句柄
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
