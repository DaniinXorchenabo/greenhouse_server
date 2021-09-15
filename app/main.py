import os
from dotenv import load_dotenv
from os.path import dirname, join, split


if os.environ.get("PG_SUPERUSER_NAME") is None:

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

path = dirname(__file__)
while "app" in (path := split(path)[0]):
    pass
path = join(path, "app", "src", "db", "picolo_conf.env")
# os.environ["PICCOLO_CONF"] = "src.db.piccolo_conf"
if os.path.exists(path):
    load_dotenv(path)


from fastapi import FastAPI
import uvicorn
from src.init_app import init_app_func
import importlib
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}


init_app_func(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)