import json

import requests as rs

# Pet store functional testing project

# TEST 1 - New pet creation
# Creating a new record in the database for a new pet, inserting all
# relevant data describing the pet.
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

# TEST 2 - Getting pet's data by ID (case: found)
# Extract the existing pet's data by ID from the Swagger database.
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

# TEST 3 - Getting pet's data by ID (case: not found)
# Extract the existing pet's data by ID from the Swagger database.
def test_get_pet_by_id_not_found():
    response = rs.get('https://petstore.swagger.io/v2/pet/0')
    pet_dict = json.loads(bytearray(response.text, 'utf-8'))
    assert response.status_code == 404
    assert pet_dict['code'] == 1
    assert pet_dict['type'] == 'error'
    assert pet_dict['message'] == 'Pet not found'

# TEST 4 - Existing pet deletion (case: existing)
# Deleting the pet's entire data record from the database Swagger,
# which exists in the database.
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

# TEST 5 - Existing pet deletion (case: non-existing)
# Deleting the pet's entire data record from the database Swagger,
# which does not exist in the database.
def test_delete_pet_not_found():
    response_delete = rs.delete('https://petstore.swagger.io/v2/pet/-400')
    assert response_delete.status_code == 404

# TEST 6 - Posting new order into the database
# Creating a new record for the pet in the database.
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

# TEST 7 - Getting order data by order ID (case: existing order)
# Extracting the data record for the existing oder by using existing order ID.
def test_get_order_by_id():
    response = rs.get('https://petstore.swagger.io/v2/store/order/4')
    pet_dict = json.loads(bytearray(response.text, 'utf-8'))
    assert response.status_code == 200
    assert pet_dict['id'] == 4
    assert pet_dict['petId'] == 5
    assert pet_dict['quantity'] == 2
    assert pet_dict['status'] == 'placed'
    assert pet_dict['complete'] == True

# TEST 8 - Getting order data by order ID (case: non-existing order)
# Extracting the data record for the non-existing oder by using non-existing order ID.
def test_get_order_by_id_not_found():
    response = rs.get('https://petstore.swagger.io/v2/store/order/-4')
    pet_dict = json.loads(bytearray(response.text, 'utf-8'))
    assert response.status_code == 404
    assert pet_dict['code'] == 1
    assert pet_dict['type'] == 'error'
    assert pet_dict['message'] == 'Order not found'

# TEST 9 - New user creation
# Create a new user in the database, insert all the relevant data while
# creating a record in the database.
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

# TEST 10 - User data update
# Update the data for the existing user.
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

# TEST 11 - User data record deletion
# Delete all data for the existng user from the database.
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
