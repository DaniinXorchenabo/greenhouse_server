from piccolo.engine import engine_finder

from src.api.add_routers import add_routers_func



def init_app_func(app):
    """Добавление событий, обработчиков исключений

    Добавление всего того, что можно добавить только к FastApi()
    и нельзя добавить к ApiRouter()"""

    # add_routers_func(app)

    @app.on_event("startup")
    async def open_database_connection_pool():
        try:
            engine = engine_finder()
            await engine.start_connection_pool()
        except Exception:
            print("Unable to connect to the database")

    @app.on_event("shutdown")
    async def close_database_connection_pool():
        try:
            engine = engine_finder()
            await engine.close_connection_pool()
        except Exception:
            print("Unable to connect to the database")




