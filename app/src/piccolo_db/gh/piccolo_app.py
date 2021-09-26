"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

import os

from piccolo.conf.apps import AppConfig, table_finder

print("************************")


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

try:
    print('try import with AppConfig tables as src.piccolo_db.gh.tables.superuser')
    APP_CONFIG = AppConfig(
        app_name="gh",
        migrations_folder_path=os.path.join(
            CURRENT_DIRECTORY, "piccolo_migrations"
        ),
        table_classes=table_finder(modules=["src.piccolo_db.gh.tables.superuser"]),
        migration_dependencies=[],
        commands=[],
    )
except ModuleNotFoundError:
    print("error! try import with AppConfig tables as gh.tables.superuser")
    piccolo_conf = os.environ.pop("PICCOLO_CONF", None)
    APP_CONFIG = AppConfig(
        app_name="gh",
        migrations_folder_path=os.path.join(
            CURRENT_DIRECTORY, "piccolo_migrations"
        ),
        table_classes=table_finder(modules=["gh.tables.superuser"]),
        migration_dependencies=[],
        commands=[],
    )
    # os.environ["PICCOLO_CONF"] = piccolo_conf
