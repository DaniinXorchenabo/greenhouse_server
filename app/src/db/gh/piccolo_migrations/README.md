Add migrations using `piccolo migrations new home --auto`.

1. выполнить миграции для создания таблиц picolo-пользователей
```
piccolo migrations forwards user
piccolo migrations forwards session_auth
```


2. создать пользователей picolo
```
python create_picolo_users.py
```
3. Настроить postgres-пользователей 


4. Выполнить все оставшиеся миграции
```
piccolo migrations forwards gh
```

5. При каждом запуске docker-compose мигрировать

6. При каждом git pull пытаться мигрировать