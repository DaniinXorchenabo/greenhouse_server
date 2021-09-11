import typing as t
from os.path import dirname, join

from piccolo_admin.endpoints import create_admin
from piccolo_api.crud.serializers import create_pydantic_model
from piccolo.engine import engine_finder
from starlette.routing import Route, Mount
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from src.api.picalo_test_app.endpoints import HomeEndpoint
from src.db.gh.piccolo_app import APP_CONFIG
# from src.db.gh.tables.superuser import Task


app = APIRouter(
    routes=[],
)


@app.get("/tasks")
async def tasks():
    return {"****************": ""}


# TaskModelIn: t.Any = create_pydantic_model(table=Task, model_name="TaskModelIn")
# TaskModelOut: t.Any = create_pydantic_model(
#     table=Task, include_default_columns=True, model_name="TaskModelOut"
# )
#
#
# @app.get("/tasks/", response_model=t.List[TaskModelOut])
# async def tasks():
#     return await Task.select().order_by(Task.id).run()
#
#
# @app.post("/tasks/", response_model=TaskModelOut)
# async def create_task(task: TaskModelIn):
#     task = Task(**task.__dict__)
#     await task.save().run()
#     return TaskModelOut(**task.__dict__)
#
#
# @app.put("/tasks/{task_id}/", response_model=TaskModelOut)
# async def update_task(task_id: int, task: TaskModelIn):
#     _task = await Task.objects().where(Task.id == task_id).first().run()
#     if not _task:
#         return JSONResponse({}, status_code=404)
#
#     for key, value in task.__dict__.items():
#         setattr(_task, key, value)
#
#     await _task.save().run()
#
#     return TaskModelOut(**_task.__dict__)
#
#
# @app.delete("/tasks/{task_id}/")
# async def delete_task(task_id: int):
#     task = await Task.objects().where(Task.id == task_id).first().run()
#     if not task:
#         return JSONResponse({}, status_code=404)
#
#     await task.remove().run()
#
#     return JSONResponse({})
#
#
#
