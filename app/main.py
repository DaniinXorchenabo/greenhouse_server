import os
from dotenv import load_dotenv
from os.path import dirname, join, split

from src.db.gh.tables import tab

if os.environ.get("PG_SUPERUSER_NAME") is None:

    path = dirname(__file__)
    while "app" in (path := split(path)[0]):
        pass

    dotenv_path = join(path, '.env')
    print(dotenv_path, __file__)
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        print("В корне проекта обязательно должен быть файл .env!!!!")
        raise FileNotFoundError("\n.env file must be in project root\n")

path = dirname(__file__)
while "app" in (path := split(path)[0]):
    pass
path = join(path, "app", "src", "db", "piccolo_conf.env")
# os.environ["PICCOLO_CONF"] = "src.db.piccolo_conf"
if os.path.exists(path):
    load_dotenv(path)


os.environ.update({key.split("#")[0].replace(" ", ""): val.split("#")[0].replace(" ", "") for key, val in os.environ.items() if not print(key, [val])} )

from typing import Any, Optional, Awaitable

from fastapi import FastAPI, Depends
import uvicorn
from src.init_app import init_app_func
import importlib
from pydantic import BaseModel

from src.db.piccolo_conf import system_engine, guest_engine
from src.api.security.check_roles import admin
from src.api.security.schemes import Tab

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}


@app.get("/status1/")
async def read_system_status(t: Tab = Depends(admin)):  # , scopes=['g', 'a']
    print("функция запроса")
    u2 = (await (u := tab.guest.User).objects().where(u.username == "Vasiliev_1").first().run())
    print("конец системной транзакции")
    return {"status": "ok", "u": t.u, "us": u2}


init_app_func(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8020, reload=True)
