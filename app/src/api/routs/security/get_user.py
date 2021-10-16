import os
from typing import Optional, Awaitable, Union, Literal

from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import SecurityScopes
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.security import verify_password
from src.api.routs.security.config import oauth2_scheme
from src.api.routs.security.schemes import TokenData
from src.db.models.connections import system_readonly_conn
from src.db.models import system
from src.db.models.sessions import system_session
from src.api.exceptions.e_401_not_authorizes import BearerNotAuthorizedError
from src.api.exceptions.e_404_not_found import PasswordOrUsernameIncorrectError
from src.api.exceptions.e_403_forbidden import NotAccessForbidden


__all__ = [
    "get_user",
    "authenticate_user",
    "get_current_user",

]

SECRET_KEY = os.environ.get("AUTH_TOKEN_SECURITY")
ALGORITHM = os.environ.get("TOKEN_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_user(username: str) -> Awaitable:
    return system.User.get_via_username(system_session, username)


async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    assert user is not None, PasswordOrUsernameIncorrectError()
    assert verify_password(password, user.hashed_password), PasswordOrUsernameIncorrectError()
    return user


async def get_current_user(
        security_scopes: SecurityScopes,
        token: str = Depends(oauth2_scheme),
):
    print('\n\n-------------', security_scopes.scopes, "\n\n")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        assert username is not None, BearerNotAuthorizedError()
        token_data = TokenData(scopes=payload.get("scopes", []), username=username)
        token_data.scopes = set(token_data.scopes)
    except (JWTError, ValidationError):
        raise BearerNotAuthorizedError(security_scopes.scope_str)

    user = await get_user(username=token_data.username)
    assert user is not None, BearerNotAuthorizedError(security_scopes.scope_str)

    # Хватает ли разрешений на доступ к этому роуту
    token_data.scopes &= set(user.scopes)
    for scope in security_scopes.scopes:
        assert scope in token_data.scopes, NotAccessForbidden()

    return user
