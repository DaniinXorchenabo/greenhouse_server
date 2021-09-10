# greenhouse_server

сервер для теплицы

## RUN

### Run with docker

1.) Create .env file in root of project (see example.env file).

2.)
```
docker-compose build
docker-compose up -d
```

### Run with local python

1.) Create .env file in root of project (see example.env file).

2.) 
```
pip install -r app/requirements/dev/requirements.txt
```

3.)
```
python app/main.py
```
or 3.)
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```