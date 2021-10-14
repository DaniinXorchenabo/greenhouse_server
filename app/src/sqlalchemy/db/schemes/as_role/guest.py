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
    # hashed_password: str
    # email: str
    # _scopes: list[Scopes]

    class Config:
        orm_mode = True


class OutUser(BaseModel):
    username: str
    name: str
    surname: str

    class Config:
        orm_mode = True


class InUser(DbUser):
    pass


