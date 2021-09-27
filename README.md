## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run uvicorn main:app --reload --host 0.0.0.0 --port $PORT
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
