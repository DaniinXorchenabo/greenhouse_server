from uuid import uuid4

from tortoise import Tortoise, fields, run_async
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.models import Model
from pydantic import BaseModel, Field, EmailStr, root_validator

from src.db.gh.system import tables as t
from src.utils.security import get_password_hash


GetUser = pydantic_model_creator(t.User)
AuthUser = pydantic_model_creator(t.User, exclude=("hashed_password",))
_CreateUser = pydantic_model_creator(t.User, exclude=("id", "hashed_password", "gh_user"))
DbUser = pydantic_model_creator(t.User)
UserQuery = pydantic_queryset_creator(t.User)


class CreateUser(_CreateUser, BaseModel):
    password: str = Field(..., regex='^.{10,}$')

    @root_validator()
    def hashing_password(cls, values: dict):
        values["hashed_password"] = get_password_hash(values.get("password", ""))
        values['id'] = uuid4()
        return values


