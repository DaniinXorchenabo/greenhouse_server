from os.path import dirname, join

from piccolo_admin.endpoints import create_admin
from starlette.routing import Route, Mount
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.api.piccolo_test_app.endpoints import HomeEndpoint
from src.db.gh.piccolo_app import APP_CONFIG
# from src.db.gh.tables.superuser import Task

from src.api.piccolo_test_app.app import app as piccolo_app
from os.path import dirname, join

from fastapi import FastAPI
from piccolo_admin.endpoints import create_admin
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from src.api.piccolo_test_app.app import app as piccolo_app
from src.api.security.app import app as security_app
from src.api.piccolo_test_app.endpoints import HomeEndpoint
from src.db.gh.piccolo_app import APP_CONFIG


# from src.db.gh.tables.superuser import Task


def add_routers_func(app: FastAPI):
    """Добавляем роуты в приложение"""
    # piccolo_app: APIRouter
    app.include_router(piccolo_app)
    app.include_router(security_app)
    app.routes.extend([
        Route("/", HomeEndpoint),
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG.table_classes,
                # Required when running under HTTPS:
                # allowed_hosts=['my_site.com']
            ),
        ),
        Mount("/static/", StaticFiles(directory=join(dirname(__file__), "piccolo_test_app", "static"))),

    ])

    # pass
