from src.utils.enums import Scopes


class ScopesForUser(object):

    @property
    def scopes(self):
        return {Scopes(i) for i in self._scopes}

    @scopes.setter
    def scopes(self, value):
        self._scopes = {Scopes(i) for i in value}