""" 协程异步任务
note1: 协程中不要涉及数据库操作, 否则需要安装sqlalchemy协程支持包
test:
    from app.utils.bamboo_asyncio import *
    bamboo_asyncio = BambooAsyncio()
    for i in range(100):
        bamboo_asyncio.add_task(test_cb, f'user{i}', i)

    for i in range(50):
        bamboo_asyncio.add_task(test_request)

    bamboo_asyncio.run()
"""
import asyncio
import time

from flask import current_app


async def test_cb(user, uid, country='china', nation='汉族'):
    asyncio.sleep(5)
    print(f'>>>user:{user}, {uid}, {country}, {nation}')


async def test_request():
    import aiohttp
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.baidu.com') as response:
            print("Status:", response.status)
            html = await response.text()
            print("Body:", html[:15], "...")


class BambooAsyncio:
    def __init__(self):
        self.loop_tasks = []

    async def async_cb(self, cb, *args, **kwargs):
        await cb(*args, **kwargs)

    def add_task(self, cb, *args, **kwargs):
        self.loop_tasks.append(asyncio.ensure_future(cb(*args, **kwargs)))

    def run(self):
        # 1. 初始化
        current_app.logger.info(f'Bamboo asyncio简单异步处理任务: running')
        start = int(time.time() * 1000)

        # 2. 启动并等待任务
        event_loop = None
        try:
            event_loop = asyncio.get_event_loop()
            event_loop.run_until_complete(asyncio.wait(self.loop_tasks))
        except Exception as msg:
            current_app.logger.exception(f'Bamboo asyncio简单异步处理任务异常:{msg}')
        finally:
            try:
                event_loop.close()
            except BaseException:
                pass

        # 3. 收尾
        end = int(time.time() * 1000)
        current_app.logger.info(
            f'Bamboo asyncio简单异步处理任务: end, 处理时长:{end - start} ms')
