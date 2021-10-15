from os.path import dirname, join

from fastapi import FastAPI

from src.api.routs import all_routers

__all__ = ['add_routers_func']


def add_routers_func(app: FastAPI):
    """Добавляем роуты в приложение"""

    [app.include_router(route) for route in all_routers]
