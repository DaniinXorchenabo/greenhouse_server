from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from src.api.exceptions.base import MyBaseHttpException


__all__ = ['add_assert_exception_handlers']


def add_assert_exception_handlers(app: FastAPI) -> FastAPI:

    @app.exception_handler(AssertionError)
    async def base_http_error(request: Request, exc: AssertionError):
        print('_*&!_+++++++++++++++++++++ASSERT', exc)
        if len(exc.args) > 0 and isinstance(exc.args[0], MyBaseHttpException):
            exc.args[0]: MyBaseHttpException
            return exc.args[0].response

    return app