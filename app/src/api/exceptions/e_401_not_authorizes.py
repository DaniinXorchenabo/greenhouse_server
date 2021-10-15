from typing import Optional

from src.api.responses.error import NotAuthorized
from src.api.exceptions.base import MyBaseHttpException

__all__ = ['BearerNotAuthorizedError']


class BaseNotAuthorizedError(MyBaseHttpException):
    default_status_code = 401
    # default_response_model =


class BearerNotAuthorizedError(BaseNotAuthorizedError):
    default_response_model = NotAuthorized
    default_headers = {'WWW-Authenticate': "Bearer"}

    def __init__(self, scopes: Optional[str] = None, *a, **k):
        if scopes is not None:
            k['headers'] = k.get('headers', dict()) | {'WWW-Authenticate': "Bearer scope=" + scopes}
        super().__init__(*a, **k)
