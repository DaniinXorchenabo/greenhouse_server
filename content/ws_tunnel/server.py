from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.route("/", methods=["GET", "POST", "PUT", "DELETE", "PATH"])
async def router():
    return {"": ""}


@app.middleware()
async def fff():
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=80, reload=True)