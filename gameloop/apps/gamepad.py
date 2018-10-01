from gameloop.apps.web import sio


@sio.on('connect', namespace='/gamepad')
def connect(sid, environ):
    print("connect ", sid)


@sio.on('action', namespace='/gamepad')
async def message(sid, data):
    print("message ", data)
    await sio.emit('reply', room=sid)


@sio.on('disconnect', namespace='/gamepad')
def disconnect(sid):
    print('disconnect ', sid)
