import os
from typing import Optional, Awaitable, Union, Literal

from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import SecurityScopes
from pydantic import ValidationError

from src.utils.security import verify_password
from src.db.gh.tables import tab
from src.api.security.config import oauth2_scheme
from src.api.security.schemes import TokenData


SECRET_KEY = os.environ.get("AUTH_TOKEN_SECURITY")
ALGORITHM = os.environ.get("TOKEN_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_user(username: str) -> Awaitable[Optional[tab.system.User]]:
    return (u := tab.system.User).objects().where(u.username == username).first().run()


async def authenticate_user(username: str, password: str) -> Union[tab.system.User, Literal[False]]:
    user = await get_user(username)
    if user is None:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


async def get_current_user(
        security_scopes: SecurityScopes,
        token: str = Depends(oauth2_scheme),
) -> tab.system.User:
    # создание ошибки авторизации
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    print('\n\n-------------', security_scopes.scopes, "\n\n")
    # получение данных из токена
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception

    # Хватает ли разрешений на досту к этому роуту
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:  # то, что пришло в токене
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user

