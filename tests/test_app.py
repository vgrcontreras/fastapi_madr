from http import HTTPStatus


def test_read_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_create_user(client):
    response = client.post(
        '/contas/',
        json={
            'username': 'test',
            'email': 'test@test.com',
            'password': 'testtest'
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
            'id': 1,
            'username': 'test',
            'email': 'test@test.com',
        }
