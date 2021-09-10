FROM python:3.9.6-slim AS builder
RUN mkdir ./app

COPY ./requirements/dev/requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt --no-cache-dir
WORKDIR ./app

#FROM python:3.9.6-alpine
#COPY ./requirements/dev/requirements.txt ./requirements.txt
#COPY --from=builder /root/.local /root/.local
#RUN pip install -r ./requirements.txt
##COPY --from=builder /lib ./lib
##COPY --from=builder /usr/local/bin ./usr/local/bin
#WORKDIR ./app