#!/usr/bin/python
# coding:utf-8
import socketserver
from socketserver import StreamRequestHandler as SRH
from time import ctime

host = '127.0.0.1'
port = 8008
addr = (host, port)


class Servers(SRH):
    def handle(self):
        print('got connection from ', self.client_address)
        self.wfile.write(
            'connection %s:%s at %s succeed!' %
            (host, port, ctime()))
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print(data)
            self.request.send(data)


print('server is running....')
server = socketserver.ThreadingTCPServer(addr, Servers)
server.serve_forever()
