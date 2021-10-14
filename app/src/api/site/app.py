from uuid import UUID
from typing import Optional

from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Body, Path, Depends

from src.db.models.connections import system_connection
from src.db.models import guest_schema, guest_session, system_schema, system as system_table, user_schema
from src.db.models import UserBox, GuestBox, AdminBox
from src.api.security.check_roles import guest, admin, user

app = APIRouter()

