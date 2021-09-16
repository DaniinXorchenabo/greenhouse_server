import asyncpg
from piccolo.engine import engine_finder
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.api.add_routers import add_routers_func
from src.db.piccolo_conf import readonly_DB


def init_app_func(app: FastAPI):
    """Добавление событий, обработчиков исключений

    Добавление всего того, что можно добавить только к FastApi()
    и нельзя добавить к ApiRouter()"""

    add_routers_func(app)

    @app.on_event("startup")
    async def open_database_connection_pool():
        try:
            engine = engine_finder()
            await engine.start_connection_pool()
            await readonly_DB.start_connection_pool()
        except Exception:
            print("Unable to connect to the database")

    @app.on_event("shutdown")
    async def close_database_connection_pool():
        try:
            engine = engine_finder()
            await engine.close_connection_pool()
            await readonly_DB.close_connection_pool()

        except Exception:
            print("Unable to connect to the database")


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




