from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from cursofastapi.schemas import Message

app = FastAPI(title='Autralopithecus API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def retornar_hello_world():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport"content="width=device-width,
    initial-scale=1.0">
    <title>Retorno</title>
    </head>
    <body>
        <h1>Hello World my friend</h1>
    </body>
    </html>
"""
