from http import HTTPStatus

from fastapi.testclient import TestClient

from cursofastapi.app import app

with open(
    '/home/pedroalvares/Git/CursoFastApi/cursofastapi/templates/index.html',
    'r',
    encoding='utf-8',
) as file:
    conteudo = file.read()


def test_root_deve_retornar_hello_world():
    client = TestClient(app)
    response = client.get('/')
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK


def test_deve_retornar_hello_world_com_html():
    client = TestClient(app)
    response = client.get('/html')

    assert response.text == conteudo
    assert response.status_code == HTTPStatus.OK


def test_create_use():
    client = TestClient(app)
    response = client.post(
        '/users/',
        json={
            'username': 'pedro',
            'email': 'pedro@email.com',
            'password': '123',
        },
    )

    assert response.json() == {
        'username': 'pedro',
        'email': 'pedro@email.com',
        'id': 1,
    }

    assert response.status_code == HTTPStatus.CREATED
