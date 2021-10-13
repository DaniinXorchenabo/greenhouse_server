from uuid import  UUID

from pydantic import BaseModel


__all__ = ["DbUser"]


class DbUser(BaseModel):
    id: UUID