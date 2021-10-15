from fastapi import APIRouter

from src.api.routs.security import app as security_app, security_tags
from src.api.routs.android import app as android_app, android_tags
from src.api.routs.site import app as site_app, tags_from_site
from src.api.routs.EXAMPLE_CRUD import app as EXAMPLE_CRUD_app, EXAMPLE_tags

tags_info: dict[str, dict[str, str]] = security_tags | android_tags | tags_from_site | EXAMPLE_tags
tags_info = {tag_name: ({"name": tag_name} | value) for tag_name, value in tags_info.items()}
__all__ = ["all_routers", "android_app", "security_app", "site_app",
           "EXAMPLE_CRUD_app", 'tags_info']


all_routers: list[APIRouter] = [android_app, security_app, site_app, EXAMPLE_CRUD_app]