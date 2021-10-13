from uuid import UUID

from fastapi import APIRouter, Path, Depends
# from fastapi

from src.api.security.check_roles import user
from src.api.security.schemes import Tab
# from src.piccolo_db.gh.tables import user as models
# from src.piccolo_db.gh import schemes as sch

__all__ = ["app"]

app = APIRouter(prefix="/user", dependencies=[Depends(user)])


# @app.get('/get_greenhouses')
# async def get_greenhouses(me: Tab = Depends(user)):
#     print("^%$$$$$$$$$---------", me)
#     return {"d":  [await i.get_related(me.t.UserGreenhouse.gh_id).run()
#                    for i in await me.t.UserGreenhouse.objects().where(me.t.UserGreenhouse.user_id == me.u.id)]}
#.where(me.t.UserGreenhouse.user_id == me.u.id)
    # return {"d" : await models.Greenhouse.raw("SELECT greenhouse.* FROM greenhouse_user  "
    #                              "LEFT JOIN greenhouse ON  greenhouse_user.gh = greenhouse.id"
    #                              "WHERE greenhouse_user.user = {}", me.u.id).run()}


@app.websocket("/greenhouse/{greenhouse_id}")
async def chatting_with_android(greenhouse_id: UUID = Path(...)):
    pass
