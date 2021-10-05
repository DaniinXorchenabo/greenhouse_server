import os

import asyncpg
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from piccolo.engine import engine_finder
from tortoise import Tortoise
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

from src.api.add_routers import add_routers_func
from src.piccolo_db.piccolo_conf import guest_engine
from src.piccolo_db.piccolo_conf import user_engine
from src.piccolo_db.piccolo_conf import admin_engine
from src.piccolo_db.piccolo_conf import developer_engine
from src.piccolo_db.piccolo_conf import system_engine
from src.connect_with_proxy import add_proxy
from src.db.tortoise_orm_config import tortoise_init
from src.db.tortoise_orm_config import config


def init_app_func(app: FastAPI):
    """Добавление событий, обработчиков исключений

    Добавление всего того, что можно добавить только к FastApi()
    и нельзя добавить к ApiRouter()"""

    add_routers_func(app)

    # @app.on_event("startup")
    # async def open_database_connection_pool():
    #     try:
    #         pass
    #         # await tortoise_init()
    #         # engines = [guest_engine, user_engine,
    #         #            admin_engine, developer_engine,
    #         #            system_engine]
    #         # [await engine.start_connection_pool(max_size=20) for engine in engines]
    #     except Exception as e:
    #         print("----Unable to connect to the database, open_database_connection_pool", e)
    #
    # @app.on_event("shutdown")
    # async def close_database_connection_pool():
    #     try:
    #         pass
    #         # engines = [guest_engine, user_engine,
    #         #            admin_engine, developer_engine,
    #         #            system_engine]
    #         # [await engine.close_connection_pool() for engine in engines]
    #         # await Tortoise.close_connections()
    #     except Exception as e:
    #         print("----Unable to connect to the database, close_database_connection_pool", e)

    @app.exception_handler(asyncpg.exceptions.InsufficientPrivilegeError)
    async def permission_error(request: Request, exc: asyncpg.exceptions.InsufficientPrivilegeError):
        """asyncpg.exceptions.InsufficientPrivilegeError: permission denied for table <my table>

        Вызывается тогда, когда пользователю базы данных не доступна
        запрашиваемая операция. К примеру, пользователь БД read-only
        (может выполнять только SELECT)
        попытался выполнить операцию SQL INSERT
        """
        return JSONResponse(
            status_code=400,
            content={"message": f"Вы не имеете доступа, необходимого для выполнения запроса"},
        )

    @app.exception_handler(asyncpg.exceptions.UniqueViolationError)
    async def permission_error(request: Request, exc: asyncpg.exceptions.UniqueViolationError):
        """asyncpg.exceptions.UniqueViolationError:
            duplicate key value violates unique constraint "<table_name>_<field_name>_key"

        Вызывается тогда, когда пользователю базы данных не доступна
        запрашиваемая операция. К примеру, пользователь БД read-only
        (может выполнять только SELECT)
        попытался выполнить операцию SQL INSERT
        """
        return JSONResponse(
            status_code=400,
            content={"message": f"Какое-то из полей запроса уже имеется в БД. Поле должно быть уникальным!"},
        )

    register_tortoise(app, config=config, add_exception_handlers=True)

    if os.environ.get("USE_PROXY", "false") == "true":
        add_proxy(app)





