FROM python:3.9.6-slim
RUN mkdir ./app
WORKDIR ./app
COPY ./requirements/dev/requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
