from datetime import timedelta
import os

from fastapi import Depends, APIRouter, HTTPException, Body
from fastapi.security import (
    OAuth2PasswordRequestForm,
)

from src.api.security.schemes import Token
from src.api.security.get_user import authenticate_user
from src.api.security.utils import create_access_token
from src.api.security.config import TOKEN_URL
from src.db.models.schemes.as_role._real import CreateUser
from src.db.models import _real
from src.db.models.sessions import system_session



__all__ = ["app"]

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.environ.get("AUTH_TOKEN_SECURITY")
ALGORITHM = os.environ.get("TOKEN_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = APIRouter()


@app.post("/" + TOKEN_URL, response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/sign_up")
async def registration(data: CreateUser = Body(...),
                       # session: AsyncSession = Depends(system_connection)
                       ):
    async with system_session() as session:
        async with session.begin():
            await _real.User.create(session, **data.dict())
    # res = await tab.system.User(**DbUser(**(data.dict() | {"scopes": [Scopes.user]})).dict()).save().run()
    return "ok"