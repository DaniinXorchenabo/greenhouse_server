# import os
#
# import asyncpg
# import asyncio
# import ssl
#
#
# from os.path import dirname,  join, split
#
#
# if os.environ.get("PG_SUPERUSER_NAME") is None:
#     from dotenv import load_dotenv
#
#     path = dirname(__file__)
#     while "app" in (path := split(path)[0]):
#         print(path)
#
#     dotenv_path = join(path, '.env')
#     print(dotenv_path, __file__)
#     if os.path.exists(dotenv_path):
#         load_dotenv(dotenv_path)
#     else:
#         print("В корне проекта обязательно должен быть файл .env!!!!")
#         raise FileNotFoundError("\n.env file must be in project root\n")
#
#
# async def main():
#     user = os.environ.get("PG_SUPERUSER_NAME")
#     pas = os.environ.get("PG_SUPERUSER_PASSWORD")
#     host = os.environ.get("PGHOST")
#     port = os.environ.get("PGPORT")
#     db = os.environ.get("PGDATABASE")
#     # host = "host.docker.internal"
#     con = await asyncpg.connect(dsn=f"postgres://{user}:{pas}@{host}:{port}/{db}")
#     # con = await asyncpg.connect(dsn=f"postgres://{user}:{pas}@{host}:{port}/{db}")
#     # **{
#     #     "database": os.environ.get("PGDATABASE"),
#     #     "user": os.environ.get("PG_SUPERUSER_NAME"),
#     #     "password": os.environ.get("PG_SUPERUSER_PASSWORD"),
#     #     "host": os.environ.get("PGHOST"),
#     #     "port": os.environ.get("PGPORT"),
#     # })
#     await con.close()
#     print("--------------------success")
#
#
# asyncio.run(main())

class A:
    is_connect = 12

class B(A):
    pass
    # is_connect = False


class C(A):
    is_connect = False


C.is_connect = True
print(C.is_connect, B.is_connect, A.is_connect)