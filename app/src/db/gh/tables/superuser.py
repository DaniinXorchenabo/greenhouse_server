from piccolo.table import Table
from piccolo.columns import Varchar, Boolean


class User(Table):
    name = Varchar()

