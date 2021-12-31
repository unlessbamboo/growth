""" 注意, flask_sockets不支持2.0+版本 """
import time
from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        print(f'收到客户端发送过来的消息:{message}')
        for i in range(100):
            ws.send(f'Hello, {message}, index:{i + 1}')
            time.sleep(0.1)


@app.route('/')
def hello():
    print('Receive a new http request')
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
