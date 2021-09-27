import time
import inspect
import asyncio

import uvicorn
from fastapi import FastAPI, Request, Response, WebSocket
from starlette.requests import empty_send, empty_receive
import dill
import h11
from httpx import AsyncClient

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
url = "ws://localhost:8000/tunnel/ws"


async def send_body(body, websocket):
    async for i in body:
        print([i])
        o = dill.dumps(i, byref=True)
        print([i], [o])
        await websocket.send(o)



async def websocket_worker():
    async with websockets.connect(url) as ws:
        websocket_pool.add(ws)
        print('сделал соединение')
        while True:
            print('ду данных')
            scope = await ws.recv()
            print('получил данные')
            r_scope = dill.loads(scope)
            r_scope["current_websocket_connection"] = ws
            try:
                print("*-----------------", r_scope)
                await app(r_scope, empty_receive, empty_send)
            except RuntimeError as e:
                print("произошла ошибка в файле tunnel.py, в websocket_worker", e)
            #
            # app.routes
            # async with AsyncClient(app=app, base_url="http://test") as ac:
            #     response = await ac.get("/")


@app.on_event("startup")
async def create_ws_pool():
    tasks = []
    for i in range(ws_pool_size):
        tasks.append(websocket_worker())
    await asyncio.gather(*tasks)
    # while True:
    #     await asyncio.sleep(1)


@app.get("/")
async def router():
    print("********************************* РОУТЕР")
    return {"": ""}


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    print("--**&6^^", response.__dict__)
    if request.scope.get("current_websocket_connection"):
        resp_body = response.body_iterator
        resp = dill.dumps(response, byref=True)

        await request.scope.get("current_websocket_connection").send(resp)
        await request.scope.get("current_websocket_connection").send(resp)
        await send_body(resp_body, request.scope.get("current_websocket_connection"))
        await request.scope.get("current_websocket_connection").send("end")
        print([resp])

    return response


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#
#     response: Response = await call_next(new_request)
#     # print(dir(response))
#     resp_body = response.body_iterator
#     resp = dill.dumps(response, byref=True)
#
#     resp_body = body_body(resp_body)
#
#     r_response = dill.loads(resp)
#     r_response.body_iterator = resp_body
#
#
#     process_time = time.time() - start_time
#     r_response.headers["X-Process-Time"] = str(process_time)
#     return r_response

""""""
# from fastapi import FastAPI, WebSocket
# from fastapi.responses import HTMLResponse
#
# app = FastAPI()
#
# html = """
# <!DOCTYPE html>
# <html>
#     <head>
#         <title>Chat</title>
#     </head>
#     <body>
#         <h1>WebSocket Chat</h1>
#         <form action="" onsubmit="sendMessage(event)">
#             <input type="text" id="messageText" autocomplete="off"/>
#             <button>Send</button>
#         </form>
#         <ul id='messages'>
#         </ul>
#         <script>
#             var ws = new WebSocket("ws://localhost:8000/tunnel/ws");
#             ws.onmessage = function(event) {
#                 var messages = document.getElementById('messages')
#                 var message = document.createElement('li')
#                 var content = document.createTextNode(event.data)
#                 message.appendChild(content)
#                 messages.appendChild(message)
#             };
#             function sendMessage(event) {
#                 var input = document.getElementById("messageText")
#                 ws.send(input.value)
#                 input.value = ''
#                 event.preventDefault()
#             }
#         </script>
#     </body>
# </html>
# """
#
#
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
#
#
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")





if __name__ == "__main__":
    # asyncio.run(create_ws_pool())
    uvicorn.run("server:app", host="localhost", port=8010, reload=True)

