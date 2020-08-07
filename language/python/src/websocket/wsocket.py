import sys
import os
import time
import asyncio
import logging

from datetime import datetime
from aiowebsocket.converses import AioWebSocket


async def startup(uri):
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        message = b'my test'
        while True:
            await converse.send(message)
            print('{time}-Client send: {message}'.format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message=message))
            mes = await converse.receive()
            print('{time}-Client receive: {message}'.format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message=mes))
            time.sleep(1)



if __name__ == '__main__':
    try:
        remote = 'wss://echo.websocket.org'
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except BaseException as exc:
        logging.info('Quite')
