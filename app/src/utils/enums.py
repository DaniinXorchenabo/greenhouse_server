from enum import Enum

class Scopes(str, Enum):
    guest = 'g'
    user = 'u'
    admin = 'a'
    dev = 'd'
    system = 's'

__all__ = ["Scopes"]

