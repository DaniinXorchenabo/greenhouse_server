import asyncpg
from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse

from src.api.exceptions.db_errors import UniqueDbBaseError, PermissionDbBaseError
from src.api.responses.error.db import UniqueDbErrorResponse, PermissionDbErrorResponse


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
        return PermissionDbBaseError().response

    @app.exception_handler(asyncpg.exceptions.UniqueViolationError)
    async def permission_error(request: Request, exc: asyncpg.exceptions.UniqueViolationError):
        """asyncpg.exceptions.UniqueViolationError:
            duplicate key value violates unique constraint "<table_name>_<field_name>_key"

        Вызывается тогда, когда пользователю базы данных не доступна
        запрашиваемая операция. К примеру, пользователь БД read-only
        (может выполнять только SELECT)
        попытался выполнить операцию SQL INSERT
        """
        return UniqueDbBaseError().response

    return app

