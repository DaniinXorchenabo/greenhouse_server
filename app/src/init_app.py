from .api.add_routers import add_routers_func


def init_app_func(app):
    """Добавление событий, обработчиков исключений

    Добавление всего того, что можно добавить только к FastApi()
    и нельзя добавить к ApiRouter()"""

    add_routers_func(app)


