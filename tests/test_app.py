from http import HTTPStatus

from fastapi.testclient import TestClient

from cursofastapi.app import app


def test_root_deve_retornar_hello_world():
    client = TestClient(app)
    response = client.get('/')
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK


# def test_deve_retornar_hello_world_com_html():
#    client1 = TestClient(app)
#    response1 = client1.get('/html')
#    assert (
#        response1.text
#        == """
#    <!DOCTYPE html>
#    <html lang="pt-br">
#    <head>
#    <meta charset="UTF-8">
#    <meta name="viewport"content="width=device-width,
#   initial-scale=1.0">
#    <title>Retorno</title>
#   </head>
#    <body>
#        <h1>Hello World my friend</h1>
#    </body>
#    </html>
# """
#    )
#    assert response1.status_code == HTTPStatus.OK
