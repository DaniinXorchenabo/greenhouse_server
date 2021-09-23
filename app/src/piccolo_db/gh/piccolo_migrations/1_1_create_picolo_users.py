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

        if os.environ.get("PG_SUPERUSER_NAME") is None:
            from dotenv import load_dotenv
            from os.path import dirname, join, split

            path = dirname(__file__)
            while "app" in (path := split(path)[0]):
                pass

            dotenv_path = join(path, '.env')
            print(dotenv_path, __file__)
            if os.path.exists(dotenv_path):
                load_dotenv(dotenv_path)
            else:
                print("В корне проекта обязательно должен быть файл .env!!!!")
                raise FileNotFoundError("\n.env file must be in project root\n")

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
