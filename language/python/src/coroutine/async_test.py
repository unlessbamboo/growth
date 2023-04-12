""" 其余更详细的例子见https://github.com/Big-universe-group/asyncio-ftwpd中说明. """

import asyncio


async def sleepN(num):
    for _i in range(10):
        print(f'----------{_i}-------------')
        await asyncio.sleep(1)
        print(f'IO结束, 回调开始{_i}======:{num}')

    return 'End:{}'.format(num)

tasks = []
for i in range(20):
    tasks.append(asyncio.ensure_future(sleepN(i)))

loop = asyncio.get_event_loop()  # 获取事件循环句柄
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
