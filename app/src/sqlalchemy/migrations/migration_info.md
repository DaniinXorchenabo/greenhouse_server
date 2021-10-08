# Init migrations

``` 
alembic --config src/sqlalchemy/migrations/alembic.ini init src/sqlalchemy/migrations/alembic  --template async 
```
# Create new bool migration

``` 
alembic --config src/sqlalchemy/migrations/alembic.ini revision -m "test"
```

# Применение всех миграций

```
alembic --config src/sqlalchemy/migrations/alembic.ini upgrade head
```