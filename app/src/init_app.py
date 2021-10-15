import os

import asyncpg
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.api import add_routers_func, handlers as error_handlers
from src.connect_with_proxy import add_proxy
from src.api.exceptions.base import MyBaseHttpException


def init_app_func(app: FastAPI):
    """Добавление событий, обработчиков исключений

    Добавление всего того, что можно добавить только к FastApi()
    и нельзя добавить к ApiRouter()"""

    add_routers_func(app)
    [handler(app) for handler in error_handlers]

    if os.environ.get("USE_PROXY", "false") == "true":
        add_proxy(app)



