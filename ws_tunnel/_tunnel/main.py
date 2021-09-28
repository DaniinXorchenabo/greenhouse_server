import asyncio
import time
import inspect
from random import randint

import uvicorn
from fastapi import FastAPI, Request, Response, WebSocket
from fastapi.responses import PlainTextResponse, JSONResponse
import dill
from fastapi.middleware.cors import CORSMiddleware
# uvicorn.
import h11


class PickleResponse(Response):
    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['body_iterator']
        return attributes


Response.__getstate__ = PickleResponse.__getstate__




websocket_control_app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8010",
]

websocket_control_app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=['*']
)


class ConnectionManager:
    ws_connections: list[WebSocket] = []
    free_ws_connection: dict[int, bool] = dict()

    @classmethod
    async def connect(cls, websocket: WebSocket):
        await websocket.accept()
        cls.ws_connections.append(websocket)
        index = len(cls.ws_connections) - 1
        cls.free_ws_connection[index] = True
        while True:
            await asyncio.sleep(randint(1, 7))
            cls.free_ws_connection[index] = False
            print("pinging")
            await websocket.send_text("ping")
            print("pinged")
            cls.free_ws_connection[index] = True



    @classmethod
    def disconnect(cls, websocket: WebSocket):
        index = cls.ws_connections.index(websocket)
        del cls.free_ws_connection[index]
        cls.ws_connections.pop(index)

    @classmethod
    async def get_body(cls, current_websocket: WebSocket):
        print("Получение тела")
        while True:

            i = await current_websocket.receive()
            print(i)
            if i.get("text") == "end":
                break
            obj = dill.loads(i['bytes'])
            print('часть тела:', obj, [obj], type(obj))
            yield obj

        print('освобождаем сокет')
        index = cls.ws_connections.index(current_websocket)
        cls.free_ws_connection[index] = True

    @classmethod
    async def send_to_server(cls, scope) -> Response:
        if len(cls.free_ws_connection) != 0:
            for key, val in cls.free_ws_connection.items():
                if val is True:
                    current_ws = cls.ws_connections[key]
                    cls.free_ws_connection[key] = False
                    break
            await current_ws.send_bytes(scope)
            # await current_ws.send_bytes(_send)

            resp = await current_ws.receive()
            print("!++++++++++++++++++++++++++++++++++++++++++++", resp)
            response: Response = dill.loads(resp['bytes'])
            print("!++++++++++++", response)
            print("----resp", response.__dict__)
            resp = await current_ws.receive()
            print("! еще раз ++++++++++++++++++++++++++++++++++++++++++++", resp)
            response: Response = dill.loads(resp['bytes'])
            print("!++++++++++++", response)
            print("----resp", response.__dict__)
            del response.headers['content-length']
            d = cls.get_body(current_ws)
            response.body_iterator = d


        else:
            response = JSONResponse({"type": "error", "details": "Не удаётся соединиться с реальным сервером"})
        return response


@websocket_control_app.websocket("/tunnel/ws")
async def create_tunnel(websocket: WebSocket):
    await ConnectionManager.connect(websocket)
    await asyncio.Future()


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#
#     del request.scope["fastapi_astack"]
#     del request.scope["app"]
#     scope = dill.dumps({"scope": request.scope}, byref=True)
#     _send = dill.dumps({"send": request._send}, byref=True)
#
#     print(scope)
#
#     current_ws = free_ws_connection.pop()
#     await current_ws.send_bytes(scope)
#     await current_ws.send_bytes(_send)
#
#     resp = await current_ws.receive()
#
#     r_response = dill.loads(resp)
#     r_response.body_iterator = get_body(current_ws)
#     return r_response


async def app(scope, receive, send):
    print(scope["type"])
    # print(*scope.items(), sep='\n')
    if scope["type"] in ["ws", "wss", "websocket"]:
        await websocket_control_app(scope, receive, send)
        return
    """
    websocket
    ('type', 'websocket')
    ('asgi', {'version': '3.0', 'spec_version': '2.1'})
    ('scheme', 'ws')
    ('server', ('127.0.0.1', 8000))
    ('client', ('127.0.0.1', 51416))
    ('root_path', '')
    ('path', '/tunnel/ws/')
    ('raw_path', '/tunnel/ws/')
    ('query_string', b'')
    ('headers', [(b'host', b'localhost:8000'), (b'upgrade', b'websocket'), (b'connection', b'Upgrade'), (b'sec-websocket-key', b'D3L8C8xy7V9288705OpHlQ=='), (b'sec-websocket-version', b'13'), (b'sec-websocket-extensions', b'permessage-deflate; client_max_window_bits'), (b'user-agent', b'Python/3.9 websockets/8.1')])
    ('subprotocols', [])
    INFO:     ('127.0.0.1', 51416) - "WebSocket /tunnel/ws/" 403
    """

    print(receive)
    print(send)

    _scope = dill.dumps(scope, byref=True)
    # _receive = dill.dumps({"receive": receive}, byref=True)
    # _send = dill.dumps({"send": send}, byref=True)
    response: Response = await ConnectionManager.send_to_server(_scope)

    await response(scope, receive, send)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}