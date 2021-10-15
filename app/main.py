from src.utils.files import check_environment_params_loaded

check_environment_params_loaded()

from fastapi import FastAPI, Depends
import uvicorn
from src.init_app import init_app_func

from src.api.routs.security.check_roles import user
from src.db.models import UserBox

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}


@app.get("/status1/")
async def read_system_status(t: UserBox = Depends(user)):  # , scopes=['g', 'a']
    print("функция запроса")
    print(t)
    # u2 = (await (u := tab.guest.User).objects().where(u.username == "Vasiliev_1").first().run())
    return {"status": "ok"}





init_app_func(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8020, reload=True)
