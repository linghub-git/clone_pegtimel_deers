from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles
from starlette.responses import FileResponse
from starlette.templating import Jinja2Templates
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware


templates = Jinja2Templates(directory='templates')

middleware = [
    Middleware(
        TrustedHostMiddleware,
        allowed_hosts=['linghub.net', '*.linghub.net'],
    ),
    Middleware(CORSMiddleware,
            allow_origins=['*'],
            allow_methods=['*']
            ),
]

def test():
    return PlainTextResponse('ok')

async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text('Hello, websocket!')
    await websocket.close()

def startup():
    print('Ready to go')

async def homepage(request):
    return templates.TemplateResponse('base.html', {'request': request})

async def research(request):
    return templates.TemplateResponse('research.html', {'request': request})

async def chykotka(request):
    return templates.TemplateResponse('chykotka.html', {'request': request})

async def library(request):
    return templates.TemplateResponse('library.html', {'request': request})

async def aboutus(request):
    return templates.TemplateResponse('present.html', {'request': request})

async def aboutus(request):
    return templates.TemplateResponse('present.html', {'request': request})

routes = [
    Route('/', endpoint=homepage),
    Route('/research', endpoint=research),
    Route('/chykotka', endpoint=chykotka),
    Route('/books', endpoint=library),
    Route('/aboutus', endpoint=aboutus),
    Route('/test', endpoint=test),
    # WebSocketRoute('/ws', websocket_endpoint),
    Mount('/static', StaticFiles(directory='static'), name='static')
]

app = Starlette(debug=True, routes=routes, middleware=middleware, on_startup=[startup])