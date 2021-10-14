from uuid import UUID
from typing import Optional

from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Body, Path, Depends

from src.sqlalchemy.db.connections import system_connection
from src.sqlalchemy.db import guest_schema, guest_session, system_schema, system as system_table, user_schema
from src.sqlalchemy.db import UserBox, GuestBox, AdminBox
from src.api.security.check_roles import guest, admin, user

app = APIRouter()

