from piccolo.table import Table
from piccolo.columns import Varchar, Boolean


class MyUser(Table):
    name = Varchar()

