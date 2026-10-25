"""
Esse recurso vai ser usado quando o arquivo for
online

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
StaticFiles(directory=BASE_DIR / 'static')
Jinja2Templates(directory=BASE_DIR / 'templates')
"""

from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from cursofastapi.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI(title='Autralopithecus API')

database = []  # banco de dados picktuflou

# Diretório contendo arquivos estáticos
app.mount(
    '/static',
    StaticFiles(
        directory='/home/pedroalvares/Git/CursoFastApi/cursofastapi/static/'
    ),
    name='static',
)

# Diretório contendo os templates Jinja
templates = Jinja2Templates(
    directory='/home/pedroalvares/Git/CursoFastApi/cursofastapi/templates/'
)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name='index.html', context={}
    )


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
