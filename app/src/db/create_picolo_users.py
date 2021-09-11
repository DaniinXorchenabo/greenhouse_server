import os
if os.environ.get("PG_SUPERUSER_NAME") is None:
    from dotenv import load_dotenv
    from os.path import dirname,  join, split

    dotenv_path = join(split(split(split(dirname(__file__))[0])[0])[0], '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        print("В корне проекта обязательно должен быть файл .env!!!!")
        FileNotFoundError("\n.env file must be in project root\n")


from piccolo.apps.user.tables import BaseUser

BaseUser(username="test",
         password="123",
         email="example@mail.com",
         active=True,
         admin=True,
         superuser=True).save().run_sync()
