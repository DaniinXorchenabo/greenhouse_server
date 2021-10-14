from uuid import  UUID, uuid4

from pydantic import BaseModel, root_validator

from src.utils.security import get_password_hash
from src.utils.enums import Scopes

__all__ = ["DbUser", "CreateUser"]


class DbUser(BaseModel):
    id: UUID
    username: str
    name: str
    surname: str
    hashed_password: str
    email: str
    _scopes: list[Scopes]


class CreateUser(BaseModel):
    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username: str
    name: str
    surname: str
    password: str
    # hashed_password = Column(String(4096), nullable=False)
    email: str
    # _scopes:

    @root_validator()
    def v(cls, values):
        values["id"] = uuid4()
        values["hashed_password"] = get_password_hash(values.pop('password'))
        values["_scopes"] = [Scopes.user]
        return values


class OutUser(DbUser):
    id: UUID
    username: str
    name: str
    surname: str
    email: str
    _scopes: list[Scopes]


class InUser(DbUser):
    id: UUID
    username: str
    name: str
    surname: str
    email: str
    _scopes: list[Scopes]


