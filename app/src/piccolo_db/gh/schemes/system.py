from uuid import uuid4, UUID
from typing import Any, Optional, Literal
from pydantic import BaseModel, validator, root_validator, Field, EmailStr

from piccolo_api.crud.serializers import create_pydantic_model
from src.utils.security import get_password_hash
from src.piccolo_db.gh.tables import system


__all__ = ["DbUser", "UserCreate"]


DbUser: Any = create_pydantic_model(table=system.User, model_name="User")
_UserCreate: Any = create_pydantic_model(
    table=(u:=system.User), model_name="_UserCreate",
    exclude_columns=(u.id, u.hashed_password, u.scopes))


class UserCreate(_UserCreate, BaseModel):
    password: str = Field(..., regex='^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[-_0-9a-zA-Z$%#^!@&*)(+=;:]{10,}$')
    email: EmailStr

    @root_validator()
    def hashing_password(cls, values: dict):
        values["hashed_password"] = get_password_hash(values.get("password", ""))
        values['id'] = uuid4()
        return values

