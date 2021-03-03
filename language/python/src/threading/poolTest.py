""" 线程池测试 """
import socket

from concurrent.futures import ThreadPoolExecutor


def echo_client(sock, client_addr):
    print('收到socket消息, 地址:', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    sock.close()


def echo_server(addr):
    # 创建线程池
    pool = ThreadPoolExecutor(128)
    sock = socket.socket(socket.AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    # 启动
    while True:
        client_sock, client_addr = sock.accept()
        # 放入池, 启动线程
        pool.submit(echo_client, client_sock, client_addr)


if __name__ == '__main__':
    # 启动服务器
    echo_server(('', 15000))
