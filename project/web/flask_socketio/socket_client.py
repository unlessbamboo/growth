""" socketio客户端标准版 """
import time
import socketio


sio = socketio.Client()
client_index = 0


@sio.event
def connect():
    print('connection established')


@sio.on('my_client_message')
def on_message(data):
    global client_index
    print('message received with ', data)
    client_index += 1
    time.sleep(1)
    sio.emit('my_message', {'name': 'bifeng', 'index': client_index})  # 发送消息


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://127.0.0.1:5000')
sio.emit('my_message', {'name': 'bifeng'})  # 发送消息
print('本次会话 ID:', sio.sid)
sio.wait()
