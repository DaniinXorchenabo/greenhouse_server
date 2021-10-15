from uuid import UUID
from typing import Optional

from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Body, Path, Depends

from src.db.models.connections import system_connection
from src.db.models import guest_schema, guest_session, system_schema, system as system_table, user_schema
from src.db.models import UserBox, GuestBox, AdminBox
from src.api.routs.security.check_roles import guest, admin, user
from src.api.responses.data import ManyUsersResponse, GetUserResponse, OkMessageResponse
from src.api.exceptions import UserNotFoundError

__all__ = ["app", "tags"]

tags = {'EXAMPLE_profile': {"description": "Пример реализации `CRUD` (Create, Read, Update, Delete) для пользователя"}}
app = APIRouter()


@app.get("/api/EXAMPLE_CRUD/users", response_model=ManyUsersResponse, tags=['EXAMPLE_profile'])
async def watch_all_products(box: GuestBox = Depends(guest)):
    return {"users": await box.t.User.all(guest_session)}


@app.get("/api/EXAMPLE_CRUD/user/{id}", response_model=GetUserResponse, tags=['EXAMPLE_profile'])
async def watch_current_product(id_: UUID, box: GuestBox = Depends(guest)):
    if (user := await box.t.User.get_via_id(guest_session, id_)) is None:
        raise UserNotFoundError()
    return {"user": user}


@app.post("/api/EXAMPLE_CRUD/user/new", response_model=GetUserResponse, tags=['EXAMPLE_profile'])
async def watch_current_product(session: AsyncSession = Depends(system_connection),
                                new_user: system_schema.CreateUser = Body(...)):
    await system_table.User.create(session, **new_user.dict())
    return new_user


@app.put("/api/EXAMPLE_CRUD/user/edit/me", response_model=GetUserResponse, tags=['EXAMPLE_profile'])
async def edit_product(updates_for_user: user_schema.UpdateMyself = Body(...),
                       box: UserBox = Depends(user)) -> user_schema.OutUser:
    await box.u.update_myself(
        box.s, (new_u := updates_for_user.dict(exclude_unset=True, exclude_defaults=True)))
    return box.u.__dict__ | new_u


@app.delete("/api/EXAMPLE_CRUD/user/delete/me", response_model=OkMessageResponse, tags=['EXAMPLE_profile'])
async def edit_product(box: UserBox = Depends(user),
                       session: AsyncSession = Depends(system_connection)):
    await box.t.User.delete(session, box.u.id)
    return OkMessageResponse()
