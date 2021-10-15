from src.api.routs import all_routers, tags_info
from src.api.exception_handlers import handlers
from src.api.add_routers import add_routers_func
from src.api.api_metadata import metadata

__all__ = ["all_routers", 'handlers', 'add_routers_func', "metadata"]

metadata['openapi_tags'] = [tags_info[tag] for tag in metadata['openapi_tags'] if tag in tags_info]
