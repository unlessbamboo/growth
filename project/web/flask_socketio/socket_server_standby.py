""" socketio服务器标准版, 实际上官方源代码examples中有几种版本的案例 """
import time
import eventlet
import socketio


sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})
server_index = 0


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def my_message(sid, data):
    global server_index
    print('message ', data)
    server_index += 1
    time.sleep(1)
    sio.emit('my_client_message', {'response': 'server', 'index': server_index})


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
