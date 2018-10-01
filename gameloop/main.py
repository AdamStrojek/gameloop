import asyncio
from threading import Thread

from aiohttp import web

from gameloop.apps.web import app, sio


async def gameloop():
    while True:
        print("Forever loop in game")
        await asyncio.sleep(1)
        await sio.emit('refresh', data=[], room='map')


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def run_http():
    web.run_app(app, host='0.0.0.0')


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(gameloop())

    new_loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(new_loop,))
    t.start()
    try:
        new_loop.call_soon_threadsafe(run_http())
    finally:
        new_loop.close()

    try:
        loop.run_forever()
    finally:
        loop.close()
