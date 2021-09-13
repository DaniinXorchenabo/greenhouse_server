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

3.) Start docker containers
```
docker-compose build
docker-compose up -d
```

4.) Check it: https://*<host from `.env` file>*:*<port from `.env` file>*, for example, [https://localhost:8000](https://localhost:8000)

### Run with local python

1.) Clone repo
```
git clone https://github.com/DaniinXorchenabo/greenhouse_server.git greenhouse_server
cd greenhouse_server
```

2.) Create `.env` file in root of project (see `example.env` file).

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

