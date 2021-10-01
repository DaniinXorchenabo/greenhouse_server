import os
import time
import inspect
import asyncio

import uvicorn
from fastapi import FastAPI, Request, Response, WebSocket
from starlette.requests import empty_send, empty_receive
import dill
from random import randint

import websockets

__all__ = ['add_proxy']

url = os.environ.get("PROXY_URL", "ws://localhost:8000/tunnel/ws")
ws_pool_size = 10


def response_getstate_(self):
    attributes = self.__dict__.copy()
    del attributes['body_iterator']
    return attributes


Response.__getstate__ = response_getstate_

websocket_pool: set = set()

socket_workers = []


class MyReceive:
    def __init__(self, current_websocket):
        self.current_websocket = current_websocket

    async def __call__(self):
        print("Получение тела")
        i = await self.current_websocket.recv()
        try:
            i = dill.loads(i)
        except TypeError:
            raise RuntimeError()
        print(i)
        if i == "end":
            return dict()
        obj = i
        # obj = dill.loads(i['bytes'])
        print('часть тела:', obj, [obj], type(obj))
        return obj


async def send_body(body, websocket):
    async for i in body:
        print([i], type(i))
        await websocket.send(i)


def add_proxy(app: FastAPI) -> FastAPI:

    async def websocket_worker():
        while True:
            try:
                async with websockets.connect(url) as ws:
                    websocket_pool.add(ws)
                    print('сделал соединение')
                    try:
                        while True:
                            scope = await ws.recv()

                            if scope == "ping":
                                continue
                            receive = MyReceive(ws)
                            print('получил данные')
                            r_scope = dill.loads(scope)
                            r_scope["current_websocket_connection"] = ws
                            try:
                                # print("*-----------------")
                                await app(r_scope, receive, empty_send)
                            except RuntimeError as e:
                                print("произошла ошибка в файле tunnel.py, в websocket_worker", e)
                    except asyncio.CancelledError:
                        await ws.close(code=1001, reason="Stopping server")
                        break
            except websockets.exceptions.ConnectionClosedError as e:
                print("Прокси разорвал соединение, пытаемся переподключиться в websocket_worker", e)
                await asyncio.sleep(1)
            except OSError as e:
                print(f"{time.ctime()}: Не удаётся подключиться к прокси серверу, websocket_worker():", e)
                await asyncio.sleep(randint(1, 30))

    @app.on_event("startup")
    async def create_ws_pool():
        for i in range(ws_pool_size):
            socket_workers.append(websocket_worker())

        await asyncio.gather(*socket_workers)

    @app.on_event('shutdown')
    async def close_ws_pool():
        for task in socket_workers:
            task.cancel()
            try:
                await task
                print('соединение с вебсокетом закрыто')
            except asyncio.CancelledError:
                print("Ошибка при закрытии корутины работника вебсокета")

    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        print(request.__dict__)

        response = await call_next(request)
        # print("--**&6^^", response.__dict__)
        if request.scope.get("current_websocket_connection"):
            resp_body = response.body_iterator
            resp = dill.dumps(response, byref=True)

            await request.scope.get("current_websocket_connection").send(resp)
            await send_body(resp_body, request.scope.get("current_websocket_connection"))
            await request.scope.get("current_websocket_connection").send("end")
            # print([resp])
        return response

    return app


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8010, reload=True)
