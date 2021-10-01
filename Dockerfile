FROM docker/compose:1.29.2
ADD content ./code/gh/
WORKDIR /code/gh
CMD docker-compose up