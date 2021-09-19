from os.path import dirname, join

from fastapi import FastAPI
from piccolo_admin.endpoints import create_admin
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from src.api.piccolo_test_app.endpoints import HomeEndpoint
from src.db.gh.piccolo_app import APP_CONFIG

from ..api import piccolo_app
from ..api import android_app
from ..api import security_app
from ..api import site_app


def add_routers_func(app: FastAPI):
    """Добавляем роуты в приложение"""

    app.include_router(piccolo_app)
    app.include_router(security_app)
    app.include_router(android_app)
    app.include_router(site_app)

    app.routes.extend([
        Route("/", HomeEndpoint),
        Mount(
            "/piccolo_admin/",
            create_admin(
                tables=APP_CONFIG.table_classes,
                # Required when running under HTTPS:
                # allowed_hosts=['my_site.com']
            ),
        ),
        Mount("/static/", StaticFiles(directory=join(dirname(__file__), "piccolo_test_app", "static"))),

    ])



