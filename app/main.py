import os
if os.environ.get("PG_SUPERUSER_NAME") is None:
    from dotenv import load_dotenv
    from os.path import dirname,  join, split

    dotenv_path = join((split(dirname(__file__))[0]), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        print("В корне проекта обязательно должен быть файл .env!!!!")
        FileNotFoundError("\n.env file must be in project root\n")

from fastapi import FastAPI
import uvicorn
from src.init_app import init_app_func

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}


init_app_func(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)