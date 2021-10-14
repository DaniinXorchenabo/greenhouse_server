from uuid import UUID
from typing import Optional

from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Body, Path, Depends

from src.sqlalchemy.db.connections import system_connection
from src.sqlalchemy.db import guest_schema, guest_session, system_schema, system as system_table, user_schema
from src.sqlalchemy.db import UserBox, GuestBox, AdminBox
from src.api.security.check_roles import guest, admin, user

__all__ = ["app"]

app = APIRouter()


@app.get("/api/EXAMPLE_CRUD/users", response_model=list[guest_schema.OutUser], tags=['profile'])
async def watch_all_products(box: GuestBox = Depends(guest)) -> list[guest_schema.OutUser]:
    return await box.t.User.all(guest_session)


@app.get("/api/EXAMPLE_CRUD/user/{id}", response_model=Optional[guest_schema.OutUser], tags=['profile'])
async def watch_current_product(id_: UUID, box: GuestBox = Depends(guest)):
    return await box.t.User.get_via_id(guest_session, id_)


@app.post("/api/EXAMPLE_CRUD/user/new", response_model=user_schema.OutUser, tags=['profile'])
async def watch_current_product(session: AsyncSession = Depends(system_connection),
                                new_user: system_schema.CreateUser = Body(...)):
    await system_table.User.create(session, **new_user.dict())
    return new_user


@app.put("/api/EXAMPLE_CRUD/user/edit/me", response_model=user_schema.OutUser, tags=['profile'])
async def edit_product(updates_for_user: user_schema.UpdateMyself = Body(...),
                       box: UserBox = Depends(user)) -> user_schema.OutUser:
    await box.u.update_myself(
        box.s, (new_u := updates_for_user.dict(exclude_unset=True, exclude_defaults=True)))
    return box.u.__dict__ | new_u


@app.delete("/api/EXAMPLE_CRUD/user/delete/me", response_model=str, tags=['profile'])
async def edit_product(box: UserBox = Depends(user),
                       session: AsyncSession = Depends(system_connection)) -> str:
    await box.t.User.delete(session, box.u.id)
    return "ok"
