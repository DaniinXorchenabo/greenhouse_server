from uuid import  UUID, uuid4
from typing import Optional

from pydantic import BaseModel, root_validator

from src.utils.security import get_password_hash
from src.utils.enums import Scopes

__all__ = ["DbUser",]


class DbUser(BaseModel):
    id: UUID
    username: str
    name: str
    surname: str
    email: str

    class Config:
        orm_mode = True


class OutUser(DbUser):
    id: UUID
    username: str
    name: str
    surname: str
    email: str

    class Config:
        orm_mode = True


class InUser(DbUser):
    id: UUID
    username: str
    name: str
    surname: str
    email: str


class UpdateMyself(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[str] = None

