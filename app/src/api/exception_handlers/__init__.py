from typing import Callable, Optional

from fastapi import FastAPI

from src.api.exception_handlers.db import add_database_exception_handlers
from src.api.exception_handlers.assert_ import add_assert_exception_handlers
from src.api.exception_handlers.http_exceptions import add_http_exception_handlers

__all__ = ['handlers', 'add_database_exception_handlers', 'add_http_exception_handlers',
           'add_assert_exception_handlers']

handlers: list[Callable[[FastAPI], Optional[FastAPI]]] = [
    add_database_exception_handlers,
    add_assert_exception_handlers,
    add_http_exception_handlers
]
