import asyncio
import time
import inspect
from random import randint
from typing import Union

import uvicorn
from fastapi import FastAPI, Request, Response, WebSocket
from fastapi.responses import PlainTextResponse, JSONResponse
import dill
from fastapi.middleware.cors import CORSMiddleware
import websockets
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
                await asyncio.sleep(randint(300, 2000)/100)
                if index in cls.free_ws_connection:
                    cls.free_ws_connection[index] = False
                    # print("pinging")
                    await websocket.send_text("ping")
                    # print("pinged")
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
    async def get_request_body(cls, receive_, current_websocket: WebSocket):
        more_body = True

        while more_body:
            message = await receive_()
            await current_websocket.send_bytes(dill.dumps(message, byref=True))
            more_body = message.get('more_body', False)
        await current_websocket.send_text("end")
        return

    @classmethod
    async def send_to_server(cls, scope, receive) -> Response:
        default_response = response = JSONResponse({"type": "error", "details": "Не удаётся соединиться с реальным сервером"})
        closed_connections = []
        if len(cls.free_ws_connection) != 0:
            while True:
                try:
                    for key, val in cls.free_ws_connection.copy().items():
                        if cls.free_ws_connection.get(key, None) is not True:
                            continue
                        print(f"key {key}, val {val}")
                        if len(cls.ws_connections) > key:
                            current_ws = cls.ws_connections[key]
                            try:
                                response = (await cls._send_to_server(scope, key, current_ws, receive)) or response
                                break
                            except AssertionError as e:
                                print("пришло сообщение на закрытие сокета")
                                cls.free_ws_connection[key] = False
                                closed_connections.append(current_ws)
                            except websockets.exceptions.ConnectionClosedError as e:
                                print("Сервер разорвал соединение. Будет использован другой websocket "
                                      "(ConnectionManager.send_to_server) :", e)
                                cls.free_ws_connection[key] = False
                                closed_connections.append(current_ws)
                        else:
                            print('длинна пула соединений меньше ключа')
                    if response == default_response:
                        print('цикл for ни разу на дошёл до работающего соединения')
                    break
                except RuntimeError as e:
                    # RuntimeError: dictionary changed size during iteration
                    # Во время итерации словарь изменил свой размер.
                    # Просто пробуем запустить еще раз
                    print("Ошибка RuntimeError в ConnectionManager.send_to_server", e)
                    pass
        else:
            print('пул соединений пуст')

        await asyncio.gather(*closed_connections)
        return response

    @classmethod
    async def _send_to_server(cls, scope, key, current_ws, receive):



        cls.free_ws_connection[key] = False
        await current_ws.send_bytes(scope)
        await cls.get_request_body(receive, current_ws)
        resp = await current_ws.receive()
        assert resp.get('type') != "websocket.disconnecte"
        if resp.get('type') and "bytes" in resp:
            print(resp)
            response: Response = dill.loads(resp['bytes'])
            del response.headers['content-length']
            d = cls.get_body(current_ws)
            response.body_iterator = d
            return response


@websocket_control_app.websocket("/tunnel/ws")
async def create_tunnel(websocket: WebSocket):
    await ConnectionManager.connect(websocket)
    # print(await websocket.receive())
    await asyncio.Future()



async def app(scope, receive, send):
    # print(scope["type"])
    # print(*scope.items(), sep='\n')
    if scope["type"] in ["ws", "wss", "websocket"]:
        await websocket_control_app(scope, receive, send)
        return

    async def read_body(receive_):
        """
        Read and return the entire body from an incoming ASGI message.
        """
        body = b''
        more_body = True

        while more_body:
            message = await receive_()
            body += message.get('body', b'')
            more_body = message.get('more_body', False)

        return body


    print("scope==================", *scope.items(), "--------", sep='\n')
    print("receive==================", receive, "--------", sep='\n')
    _scope = dill.dumps(scope, byref=True)
    # _receive = dill.dumps({"receive": receive}, byref=True)
    # _send = dill.dumps({"send": send}, byref=True)
    response: Response = await ConnectionManager.send_to_server(_scope, receive)

    await response(scope, receive, send)


if __name__ == "__main__":
    import os

    uvicorn.run("main:app", host="0.0.0.0", port=os.environ.get("PORT", 8000), reload=True)
