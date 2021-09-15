from piccolo.table import Table
from piccolo.columns import Varchar, Boolean

from src.db.piccolo_conf import readonly_DB


class MyUser(Table, db=readonly_DB):
    name = Varchar()