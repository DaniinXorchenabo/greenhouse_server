import asyncio
import time
from random import randint
from typing import Union

from fastapi import FastAPI, Request, Response, WebSocket
from fastapi.responses import PlainTextResponse, JSONResponse
import dill
from fastapi.middleware.cors import CORSMiddleware
import websockets


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

# websocket_control_app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=False,
#     allow_methods=["*"],
#     allow_headers=["*"],
#     expose_headers=['*']
# )


class ConnectionManager:
    ws_connections: list[Union[WebSocket, None]] = []
    free_ws_connection: dict[int, bool] = dict()

    @classmethod
    async def connect(cls, websocket: WebSocket):
        await websocket.accept()
        cls.ws_connections.append(websocket)
        index = len(cls.ws_connections) - 1
        cls.free_ws_connection[index] = True
        try:
            while True:
                await asyncio.sleep(randint(1, 7))
                if index in cls.free_ws_connection:
                    cls.free_ws_connection[index] = False
                    print("pinging")
                    await websocket.send_text("ping")
                    print("pinged")
                    cls.free_ws_connection[index] = True
                else:
                    break
        except websockets.exceptions.ConnectionClosedError as e:
            print("Сервер разорвал соединение (ConnectionManager.connect) :", e)
            await cls.disconnect(websocket)


        async def _lambda():
            """Обертка для неблокирующего выполнения asyncio.gather"""
            pass

        asyncio.create_task(_lambda())

    @classmethod
    async def disconnect(cls, websocket: WebSocket):
        try:
            index = cls.ws_connections.index(websocket)
            del cls.free_ws_connection[index]
            cls.ws_connections[index] = None
            await websocket.close()
        except KeyError as e:
            print("")

    @classmethod
    async def get_body(cls, current_websocket: WebSocket):
        print("Получение тела")
        while True:

            i = await current_websocket.receive()
            print(i)
            if i.get("text") == "end":
                break
            obj = i['bytes']
            # obj = dill.loads(i['bytes'])
            print('часть тела:', obj, [obj], type(obj))
            yield obj

        print('освобождаем сокет')
        index = cls.ws_connections.index(current_websocket)
        cls.free_ws_connection[index] = True

    @classmethod
    async def send_to_server(cls, scope) -> Response:
        response = JSONResponse({"type": "error", "details": "Не удаётся соединиться с реальным сервером"})
        if len(cls.free_ws_connection) != 0:
            while True:
                try:
                    for key, val in cls.free_ws_connection.items():
                        print(f"key {key}, val {val}")
                        if val is True and len(cls.ws_connections) > key:
                            current_ws = cls.ws_connections[key]
                            try:
                                cls.free_ws_connection[key] = False
                                await current_ws.send_bytes(scope)
                                resp = await current_ws.receive()
                                # print("! еще раз +++++++++++", resp)
                                if resp.get('type'):
                                    response: Response = dill.loads(resp['bytes'])
                                    # print("----resp", response.__dict__)
                                    del response.headers['content-length']
                                    d = cls.get_body(current_ws)
                                    response.body_iterator = d
                                    break
                                elif resp.get('type') == "websocket.disconnecte":
                                    await cls.disconnect(current_ws)

                            except websockets.exceptions.ConnectionClosedError as e:
                                print("Сервер разорвал соединение. Будет использован другой websocket "
                                      "(ConnectionManager.send_to_server) :", e)
                                await cls.disconnect(current_ws)
                    break
                except RuntimeError as e:
                    # RuntimeError: dictionary changed size during iteration
                    # Во время итерации словарь изменил свой размер.
                    # Просто пробуем запустить еще раз
                    print("Ошибка RuntimeError в ConnectionManager.send_to_server", e)
                    pass

        return response


@websocket_control_app.websocket("/tunnel/ws")
async def create_tunnel(websocket: WebSocket):
    await ConnectionManager.connect(websocket)
    # print(await websocket.receive())
    await asyncio.Future()



async def app(scope, receive, send):
    print(scope["type"])
    # print(*scope.items(), sep='\n')
    if scope["type"] in ["ws", "wss", "websocket"]:
        await websocket_control_app(scope, receive, send)
        return

    print(receive)
    print(send)

    _scope = dill.dumps(scope, byref=True)
    # _receive = dill.dumps({"receive": receive}, byref=True)
    # _send = dill.dumps({"send": send}, byref=True)
    response: Response = await ConnectionManager.send_to_server(_scope)

    await response(scope, receive, send)
