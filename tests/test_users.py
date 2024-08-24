from http import HTTPStatus


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
