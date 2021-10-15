from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from src.api.exceptions.base import MyBaseHttpException
from src.api.exceptions.e_401_not_authorizes import BearerNotAuthorizedError
import starlette


__all__ = ['add_http_exception_handlers']


def add_http_exception_handlers(app: FastAPI) -> FastAPI:

    @app.exception_handler(MyBaseHttpException)
    async def base_http_error(request: Request, exc: MyBaseHttpException):
        print('htttttttttttttttttp', exc)
        # return JSONResponse(content=exc.detail.dict(), status_code=exc.status_code, headers=exc.headers)
        return exc.response

    @app.exception_handler(401)
    async def bearer_not_authorized_error(request: Request, exc: HTTPException):
        if not isinstance(exc, MyBaseHttpException):
            return BearerNotAuthorizedError(headers=exc.headers).response

    return app