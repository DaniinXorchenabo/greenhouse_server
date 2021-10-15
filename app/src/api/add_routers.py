from os.path import dirname, join

from fastapi import FastAPI

from .routs import android_app
from .routs import security_app
from .routs import site_app
from .routs import EXAMPLE_CRUD_app


def add_routers_func(app: FastAPI):
    """Добавляем роуты в приложение"""

    app.include_router(EXAMPLE_CRUD_app)
    app.include_router(security_app)
    app.include_router(android_app)
    app.include_router(site_app)




