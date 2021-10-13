from src.utils.files import check_environment_params_loaded

check_environment_params_loaded()

from typing import Any, Optional, Awaitable
from fastapi import FastAPI, Depends
import uvicorn
from src.init_app import init_app_func
import importlib
from pydantic import BaseModel

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
