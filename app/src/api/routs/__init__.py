from fastapi import APIRouter

from src.api.routs.security import app as security_app
from src.api.routs.android import app as android_app
from src.api.routs.site import app as site_app
from src.api.routs.EXAMPLE_CRUD import app as EXAMPLE_CRUD_app


__all__ = ["all_routers", "android_app", "security_app", "site_app", "EXAMPLE_CRUD_app"]


all_routers: list[APIRouter] = [android_app, security_app, site_app, EXAMPLE_CRUD_app]