from pathlib import Path
import jinja2
from aiohttp import web
import socketio
import aiohttp_jinja2

templates_path = (Path(__file__) / "../../templates").resolve()

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(templates_path)))


async def index(request):
    """Serve the client-side application."""
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


class GamepadView(web.View):
    @aiohttp_jinja2.template("gamepad.html")
    async def get(self):
        context = {}
        return context


app.router.add_static('/static', 'static')
app.router.add_get('/', index)
app.router.add_view('/gamepad', GamepadView)
