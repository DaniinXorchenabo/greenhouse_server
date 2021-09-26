FROM docker/compose:1.29.2

RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf
#RUN locale-gen en_US.UTF-8

ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

# +Timezone (если надо на этапе сборки)
ENV TZ Europe/Moscow

ADD . ./code/gh/
WORKDIR /code/gh
#CMD docker-compose up



#>docker build -t daniinxorchenabo/compose_into_docker .
# docker run -itd --env-file=G:\programs\jobs\greenhouse_server_fix_bugs\content/.env -v /var/run/docker.sock:/var/run/docker.sock -v G:\programs\jobs\greenhouse_server_fix_bugs\content/:/var/tmp/  docker/compose:1.24.1  -f /var/tmp/build-docker-compose.yml up -d
# docker run -itd  --env-file=G:\programs\jobs\greenhouse_server_fix_bugs\content/.env -v /var/run/docker.sock:/var/run/docker.sock daniinxorchenabo/compose_into_docker -f /content/build-docker-compose.yml up -d