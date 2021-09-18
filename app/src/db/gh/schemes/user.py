from typing import Any

from piccolo_api.crud.serializers import create_pydantic_model

from src.db.gh.tables import user


User: Any = create_pydantic_model(table=user.User, model_name="User")
UserOut: Any = create_pydantic_model(table=user.User, model_name="UserOut",
                                     exclude_columns=(user.User.id,))
UserCreate: Any = create_pydantic_model(table=user.User, model_name="UserCreate",
                                        exclude_columns=(user.User.id,))
