""" websocket 简单示例--ssh
python版本: 3.8
"""
import time
import asyncio
import websockets


_g_connect_number = 0
MAX_MSG_IDNEX = 10000


async def hello(websocket, path):
    """ 基本echo 服务 """
    global _g_connect_number  # pylint: disable=global-statement

    _name = await websocket.recv()
    _g_connect_number += 1
    print(f'< 收到消息:{_name}, 序号:{_g_connect_number}')

    max_msg_number = 100
    for i in range(max_msg_number):
        greeting = f'你好{_name}, 你是第{_g_connect_number}号用户, 目前回传消息序号:{i + 1}'
        await websocket.send(greeting)
        print(f'> {greeting}')
        time.sleep(1)
    print('------------等待新的连接------------')


start_server = websockets.serve(hello, '0.0.0.0', 8003)  # pylint: disable=no-member
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
