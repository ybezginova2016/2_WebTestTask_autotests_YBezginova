import json

import requests as rs

def test_create_new_pet():
    pet = {
        'id': None,
        'category': {
            'id': 0,
            'name': 'string'
        },
        'name': 'doggie',
        'photoUrls': [
            'string'
        ],
        'tags': [
            {
                'id': 0,
                'name': 'string'
            }
        ],
        'status': 'available'
    }

    response = rs.post('https://petstore.swagger.io/v2/pet', json=pet)
    pet_dict = json.loads(bytearray(response.text, 'utf-8'))
    assert response.status_code == 200
    assert pet_dict['id'] is not None
    assert pet_dict['name'] == 'doggie'
    assert pet_dict['status'] == 'available'
    assert pet_dict['category']['id'] == 0
    assert pet_dict['category']['name'] == 'string'


def test_get_pet_by_id():
    pet = {
        'id': None,
        'category': {
            'id': 0,
            'name': 'string'
        },
        'name': 'doggie',
        'photoUrls': [
            'string'
        ],
        'tags': [
            {
                'id': 0,
                'name': 'string'
            }
        ],
        'status': 'available'
    }

    response_post = rs.post('https://petstore.swagger.io/v2/pet', json=pet)
    id = json.loads(bytearray(response_post.text, 'utf-8'))['id']
    response = rs.get(f'https://petstore.swagger.io/v2/pet/{id}')
    pet_dict = json.loads(bytearray(response.text, 'utf-8'))
    assert response.status_code == 200
    assert pet_dict['id'] == id
    assert pet_dict['name'] == 'doggie'
    assert pet_dict['status'] == 'available'
    assert pet_dict['category']['id'] == 0
    assert pet_dict['category']['name'] == 'string'


def test_get_pet_by_id_not_found():
    response = rs.get('https://petstore.swagger.io/v2/pet/0')
    pet_dict = json.loads(bytearray(response.text, 'utf-8'))
    assert response.status_code == 404
    assert pet_dict['code'] == 1
    assert pet_dict['type'] == 'error'
    assert pet_dict['message'] == 'Pet not found'


def test_delete_pet():
    pet = {
        'id': None,
        'category': {
            'id': 0,
            'name': 'string'
        },
        'name': 'doggie',
        'photoUrls': [
            'string'
        ],
        'tags': [
            {
                'id': 0,
                'name': 'string'
            }
        ],
        'status': 'available'
    }

    response_post = rs.post('https://petstore.swagger.io/v2/pet', json=pet)
    pet_id = json.loads(bytearray(response_post.text, 'utf-8'))['id']
    response_delete = rs.delete(f'https://petstore.swagger.io/v2/pet/{pet_id}')
    assert response_post.status_code == 200
    assert response_delete.status_code == 200


def test_delete_pet_not_found():
    response_delete = rs.delete('https://petstore.swagger.io/v2/pet/-400')
    assert response_delete.status_code == 404


def test_create_new_order():
    order = {
        'id': None,
        'petId': 0,
        'quantity': 0,
        'shipDate': '2022-11-06T13:34:52.816Z',
        'status': 'placed',
        'complete': True
    }

    response = rs.post('https://petstore.swagger.io/v2/store/order', json=order)
    order_dict = json.loads(bytearray(response.text, 'utf-8'))
    assert response.status_code == 200
    assert order_dict['id'] is not None
    assert order_dict['petId'] == 0
    assert order_dict['quantity'] == 0
    assert order_dict['status'] == 'placed'
    assert order_dict['complete'] == True


def test_get_order_by_id():
    response = rs.get('https://petstore.swagger.io/v2/store/order/4')
    pet_dict = json.loads(bytearray(response.text, 'utf-8'))
    assert response.status_code == 200
    assert pet_dict['id'] == 4
    assert pet_dict['petId'] == 5
    assert pet_dict['quantity'] == 2
    assert pet_dict['status'] == 'placed'
    assert pet_dict['complete'] == True


def test_get_order_by_id_not_found():
    response = rs.get('https://petstore.swagger.io/v2/store/order/-4')
    pet_dict = json.loads(bytearray(response.text, 'utf-8'))
    assert response.status_code == 404
    assert pet_dict['code'] == 1
    assert pet_dict['type'] == 'error'
    assert pet_dict['message'] == 'Order not found'


def test_create_new_user():
    user = {
        'id': None,
        'username': 'ybezginova',
        'firstName': 'Yulia',
        'lastName': 'Bezginova',
        'email': 'string',
        'password': 'string',
        'phone': 'string',
        'userStatus': 0
    }

    response = rs.post('https://petstore.swagger.io/v2/user', json=user)
    assert response.status_code == 200


def test_update_user():
    user = {
        'id': 0,
        'username': 'ybezginova',
        'firstName': 'Yulia',
        'lastName': 'Bezginova',
        'email': 'string',
        'password': 'string',
        'phone': 'string',
        'userStatus': 0
    }
    user_update = {
        'id': 0,
        'username': 'ybezginova',
        'firstName': 'yulia',
        'lastName': 'bezginova',
        'email': 'my_mail@gmail.com',
        'password': 'string',
        'phone': 'string',
        'userStatus': 0
    }
    response_post = rs.post('https://petstore.swagger.io/v2/user', json=user)
    response_put = rs.put('https://petstore.swagger.io/v2/user/ybezginova', json=user_update)
    assert response_post.status_code == 200
    assert response_put.status_code == 200


def test_delete_user():
    user = {
        'id': 0,
        'username': 'ybezginova',
        'firstName': 'Yulia',
        'lastName': 'Bezginova',
        'email': 'string',
        'password': 'string',
        'phone': 'string',
        'userStatus': 0
    }

    response_post = rs.post('https://petstore.swagger.io/v2/user', json=user)
    response_delete = rs.delete('https://petstore.swagger.io/v2/user/ybezginova')
    assert response_post.status_code == 200
    assert response_delete.status_code == 200
