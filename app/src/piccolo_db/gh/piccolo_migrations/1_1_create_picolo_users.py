from piccolo.apps.migrations.auto import MigrationManager


ID = "2021-09-12T00:09:31:419094"
VERSION = "0.45.1"
DESCRIPTION = "Создание пользователей для piccolo piccolo_db admin"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="", description=DESCRIPTION
    )

    def run():
        import os

        os.system("piccolo migrations forwards user && piccolo migrations forwards session_auth")

        from src.utils.files import check_environment_params_loaded

        check_environment_params_loaded()

        from piccolo.apps.user.tables import BaseUser


        BaseUser(username=os.environ.pop("PICCOLO_SUPERUSER_LOGIN"),
                 password=os.environ.pop("PICCOLO_SUPERUSER_PASSWORD"),
                 email=os.environ.pop("PICCOLO_SUPERUSER_EMAIL"),
                 active=True,
                 admin=True,
                 superuser=True).save().run_sync()

        BaseUser(username=os.environ.pop("PICCOLO_ADMIN_LOGIN"),
                 password=os.environ.pop("PICCOLO_ADMIN_PASSWORD"),
                 email=os.environ.pop("PICCOLO_ADMIN_EMAIL"),
                 active=True,
                 admin=True,
                 superuser=False).save().run_sync()

        BaseUser(username=os.environ.pop("PICCOLO_USER_LOGIN"),
                 password=os.environ.pop("PICCOLO_USER_PASSWORD"),
                 email=os.environ.pop("PICCOLO_USER_EMAIL"),
                 active=True,
                 admin=False,
                 superuser=False).save().run_sync()

    manager.add_raw(run)

    return manager
