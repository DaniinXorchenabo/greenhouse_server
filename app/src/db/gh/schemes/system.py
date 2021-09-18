from uuid import uuid4, UUID
from typing import Any, Optional
from pydantic import BaseModel, validator, root_validator, Field

from piccolo_api.crud.serializers import create_pydantic_model
from src.utils.security import get_password_hash
from src.db.gh.tables import system


DbUser: Any = create_pydantic_model(table=system.User, model_name="User")
_UserCreate: Any = create_pydantic_model(
    table=(u:=system.User), model_name="_UserCreate",
    exclude_columns=(u.id, u.hashed_password, u.scopes))


class UserCreate(_UserCreate, BaseModel):
    id:  Optional[UUID] = Field(None, title="Этот параметр передавать не нужно",
                                           example="Этот параметр передавать не нужно")
    password: str
    hashed_password: Optional[str] = Field(None, title="Этот параметр передавать не нужно",
                                           example="Этот параметр передавать не нужно")

    @root_validator()
    def hashing_password(cls, values: dict):
        values["hashed_password"] = get_password_hash(values["password"])
        values['id'] = uuid4()
        return values

