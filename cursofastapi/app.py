#correção dos diretórios static e templates
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from cursofastapi.schemas import Message


app = FastAPI(title='Autralopithecus API')

# Diretório contendo arquivos estáticos
app.mount(
    '/static',
    StaticFiles(directory=BASE_DIR / 'static'),
    name='static',
)

# Diretório contendo os templates Jinja
templates = Jinja2Templates(directory=BASE_DIR / 'templates')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name='index.html', context={}
    )
