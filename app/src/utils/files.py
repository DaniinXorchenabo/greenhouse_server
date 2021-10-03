import os
from dotenv import load_dotenv
from os.path import dirname, join, split


def load_env():
    if os.environ.get("PG_SUPERUSER_NAME") is None:

        path = dirname(__file__)
        while "app" in (path := split(path)[0]):
            pass

        dotenv_path = join(path, '.env')
        print(dotenv_path, __file__)
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        else:

            example_env = dotenv_path.replace('.env', 'example.env')

            print("В корне проекта обязательно должен быть файл .env!!!!")
            raise FileNotFoundError("\n.env file must be in project root\n")

    path = dirname(__file__)
    while "app" in (path := split(path)[0]):
        pass

    path = join(path, "app", "src", "piccolo_db", "piccolo_conf.env")
    # os.environ["PICCOLO_CONF"] = "src.piccolo_db.piccolo_conf"
    if os.path.exists(path):
        load_dotenv(path)

    os.environ.update(
        {key.split("#")[0].replace(" ", ""): val.split("#")[0].replace(" ", "")
         for key, val in os.environ.items()})


def generate_sql_migration_query():
    pass