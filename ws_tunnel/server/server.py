import time
import inspect
import asyncio

import uvicorn
from fastapi import FastAPI, Request, Response, WebSocket
from starlette.requests import empty_send, empty_receive
import dill
import h11
from httpx import AsyncClient
from random import randint

import websockets


ws_pool_size = 10


class PickleResponse(Response):
    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['body_iterator']
        return attributes


Response.__getstate__ = PickleResponse.__getstate__

websocket_pool: set = set()

app = FastAPI()
# url = "wss://gh1proxy.herokuapp.com/tunnel/ws"
url = "ws://localhost:8000/tunnel/ws"

socket_workers = []


async def send_body(body, websocket):
    async for i in body:
        print([i])
        # o = dill.dumps(i, byref=True)
        # print([i], [o])
        await websocket.send(i)


async def websocket_worker():
    while True:
        try:
            async with websockets.connect(url) as ws:
                websocket_pool.add(ws)
                print('сделал соединение')
                # await asyncio.sleep(10)

                await ws.ping()
                print("пинг")
                # await asyncio.sleep(2)
                try:
                    while True:
                        # print('жду данных')
                        scope = await ws.recv()
                        if scope == "ping":
                            continue
                        print('получил данные', scope)
                        r_scope = dill.loads(scope)
                        r_scope["current_websocket_connection"] = ws
                        try:
                            print("*-----------------", r_scope)
                            await app(r_scope, empty_receive, empty_send)
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


@app.get("/")
async def router():
    return {"": ""}


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    print("--**&6^^", response.__dict__)
    if request.scope.get("current_websocket_connection"):
        resp_body = response.body_iterator
        resp = dill.dumps(response, byref=True)

        await request.scope.get("current_websocket_connection").send(resp)
        await send_body(resp_body, request.scope.get("current_websocket_connection"))
        await request.scope.get("current_websocket_connection").send("end")
        print([resp])

    return response


if __name__ == "__main__":
    # asyncio.run(create_ws_pool())
    uvicorn.run("server:app", host="localhost", port=8010, reload=True)
