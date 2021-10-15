import asyncpg
from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse


__all__ = ['add_database_exception_handlers']


def add_database_exception_handlers(app: FastAPI) -> FastAPI:

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

    return app

