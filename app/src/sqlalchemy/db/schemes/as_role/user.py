from uuid import  UUID, uuid4

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


class OutUser(DbUser):
    username: str
    name: str
    surname: str
    email: str


class InUser(DbUser):
    username: str
    name: str
    surname: str
    email: str


