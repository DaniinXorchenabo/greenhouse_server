# Greenhouse server

Сервер для умной теплицы

## Run

----
### Run with docker

0.) [Install docker](https://docs.docker.com/engine/install/)

1.) Clone repo
```
git clone https://github.com/DaniinXorchenabo/greenhouse_server.git greenhouse_server
cd greenhouse_server
```
2.) Create `.env` file in root of project (see `example.env` file).

+ *Вы должны __обязательно__ создать новый файл, а не переименовывать старый! Это очень важно!*

+ *Войдите в новый файл и заполните __ВСЕ__ пропущенные поля!!! Впишите свои данные в строчки, где после
`=` нет значений. Между названием переменной, знаком `=` и значением __не должно быть__ 
пробелов!!! Это может иметь значение в некоторых системах!*

+ *В строчке с переменной также не должно быть комментариев (Любой текст после символа `#`)
Это также может быть критично для некоторых систем!!!*

3.) Start docker containers
```
docker-compose up -d
```

4.) Check it: https://*<host from `.env` file>*:*<port from `.env` file>*, for example, [https://localhost:8000](https://localhost:8000)

### Run with local python

1.) Clone repo
```
git clone https://github.com/DaniinXorchenabo/greenhouse_server.git greenhouse_server
cd greenhouse_server
```

2.) Create `.env` file in root of project (see `example.env` file). Change connect postgres params for success connection.

+ *Вы должны __обязательно__ создать новый файл, а не переименовывать старый! Это очень важно!*

+ *Войдите в новый файл и заполните __ВСЕ__ пропущенные поля!!! Впишите свои данные в строчки, где после
`=` нет значений. Между названием переменной, знаком `=` и значением __не должно быть__ 
пробелов!!! Это может иметь значение в некоторых системах!*

+ *В строчке с переменной также не должно быть комментариев (Любой текст после символа `#`)
Это также может быть критично для некоторых систем!!!*
  
3.) Install requirements
```
pip install -r app/requirements/dev/requirements.txt
```

4.) Run application
```
python app/main.py
```
or 4.) Ran server with `uvicorn`
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

5.) Check it: [https://localhost:8000](https://localhost:8000)

# Administration

----------------------------
## Piccolo admin

You can check it: [https://localhost:8000/admin](https://localhost:8000/admin)

![image](https://user-images.githubusercontent.com/45897837/133110838-33c93a4d-417f-4c92-88bf-9c3b3d6e978e.png)

You can get access to database controle

![image](https://user-images.githubusercontent.com/45897837/133111291-8542d8f1-941c-48dc-97cf-81d83be6af29.png)

![image](https://user-images.githubusercontent.com/45897837/133111531-8bfa0361-8cb6-4b96-ba35-bf9b748ff9f3.png)

You can touch it here: [demo1.piccolo-orm.com](https://demo1.piccolo-orm.com/#/login)

- login: piccolo
- password: piccolo123

Learn more: [click](https://piccolo-api.readthedocs.io/en/latest/index.html)

## PgAdmin
*You need in run with docker-compose for in-build PgAdmin*

Check it: [http://localhost:8080/](http://localhost:8080/)

![image](https://user-images.githubusercontent.com/45897837/133112732-d0f2ebed-717a-474d-a2a4-bf3cacafa305.png)

*login and password you can find in `.env` file*

![image](https://user-images.githubusercontent.com/45897837/133112945-b0fad89f-cc78-4ffd-88ab-c485f63deb94.png)

`PgAdmin` help you administration the database

You can learn more this: [https://linuxhint.com/postgresql_docker/](https://linuxhint.com/postgresql_docker/)


# Documentation

---------------------------

Check it: /docs [http://localhost:8040/docs](http://localhost:8040/docs) (You need in changeing 8040 to your port)

![image](https://user-images.githubusercontent.com/45897837/133885439-ac18f257-88c3-48c3-bfea-6cff1a8e4086.png)

![image](https://user-images.githubusercontent.com/45897837/133885621-22e6f57a-e701-4bb9-9f8d-3b271edfe54d.png)

It was genereted by fast-api framework, use openAPI standart

Or, You can use /redoc [http://localhost:8040/redoc](http://localhost:8040/redoc)

![image](https://user-images.githubusercontent.com/45897837/133885560-0fe2c0c3-19be-4493-99a2-d873bbc4104a.png)

It was genereted by fast-api framework too





