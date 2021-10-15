from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from src.api.exceptions.base import MyBaseHttpException


__all__ = ['add_http_exception_handlers']


def add_http_exception_handlers(app: FastAPI) -> FastAPI:

    @app.exception_handler(MyBaseHttpException)
    async def base_http_error(request: Request, exc: MyBaseHttpException):
        return JSONResponse(content=exc.detail.dict(), status_code=exc.status_code, headers=exc.headers)

    return app
