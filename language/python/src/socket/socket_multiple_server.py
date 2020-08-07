"""
一个简单的socket server 多线程服务器
"""

import os
import sys
import time
import datetime
import errno
import socket
import threading
import logging


EOL1 = b'\n\n'
EOL2 = b'\r\n'
body = """你就是个超级无敌的<em>Cool Boy<em>"""
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
response_param = [
    'HTTP/1.0 200 OK',
    'Date: {}'.format(datetime.datetime.now(datetime.timezone.utc).strftime(GMT_FORMAT)),
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {}\r\n'.format(len(body.encode('utf8'))),
    body,
]


def handle_context(conn, addr):
    """ 处理客户端发送过来的连接请求 """
    # 故意暂停线程处理时长, 以判断多线程是否正常
    print('Begin----------')
    time.sleep(20)
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)

    str_request = request.decode('utf8').split('\r\n')
    print('请求数据:\n{}'.format('\n'.join('{}'.format(k) for k in str_request)))
    response = '\r\n'.join(response_param).encode('utf8')
    conn.send(response)
    print('响应数据:\n{}'.format('\n'.join('{}'.format(k) for k in response_param)))
    print('***' * 10)
    conn.close()

 
def main():
    """ 监听指定的端口, 启动一个简单的socket监听服务器 """
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(10)
    # 设置为非阻塞模式
    #  serversocket.setblocking(0)
    
    print('Start server: http://127.0.0.1:8000')
    thread_index = 1
    try: 
        while True:
            try:
                print('~~~~~~~~~~~~~~~~')
                conn, address = serversocket.accept()
            except socket.error as e:
                if e.args[0] == errno.EAGAIN:
                    raise
                continue
            thread_index+=1
            t = threading.Thread(target=handle_context, args=(conn, address), name='thread_{}'.format(thread_index))
            t.start()
    except BaseException as e:
        logging.exception(e)
    finally:
        serversocket.close()


def streamPrint():
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
    logging.getLogger('').addHandler(console)


if __name__ == '__main__':
    streamPrint()
    main()
