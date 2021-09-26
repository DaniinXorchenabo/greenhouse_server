from fastapi.security import OAuth2PasswordBearer
from src.utils.enums import Scopes

__all__ = ["TOKEN_URL", "oauth2_scheme"]

TOKEN_URL = "token"

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=TOKEN_URL,
    scopes={
        Scopes.guest: "Незалогиненый пользователь",
        Scopes.user: "Залогиненый пользователь",
        Scopes.admin: "Администратор",
        Scopes.dev: "Разработчик",
    },
)