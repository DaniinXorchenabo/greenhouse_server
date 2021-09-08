from fastapi import FastAPI
import uvicorn

# from .src.init_app import init_app_func


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}


# init_app_func(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)