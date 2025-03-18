import pytest
from flask.testing import FlaskClient
from flask_crud_ops import app, items

@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_items(client: FlaskClient):
    response = client.get('/items')
    assert response.status_code == 200
    assert response.is_json
    assert len(response.get_json()) == len(items)


def test_get_an_item(client: FlaskClient):
    response = client.get('/items/1')
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json()['id'] == 1
    assert response.get_json()['name'] == 'Item 1'

    response = client.get('/items/999')
    assert response.status_code == 404
    assert response.is_json
    assert response.get_json()['Error'] == 'Item not found'


def test_create_item(client: FlaskClient):
    add_item: dict[str, str | int] = {
        'id': 3, 
        'name': 'Item 3', 
        'description': 'This is item 3'
        }
    response = client.post('/items', json = add_item)
    assert response.status_code == 201
    assert response.is_json
    assert response.get_json()['item'] == add_item

    for key in ('id', 'name', 'description'):           
        # (a) check for empty payload structure
        response = client.post('/items', json = {})          
        assert response.status_code == 400
        print(f'✅ Status code is 400 when {key} is missing')
        assert response.is_json
        assert response.get_json()['Error'] == 'Invalid payload structure, key names missed'

        # (b) check for invalid payload structure - deleting 'id' which is the primary key should make the payload as invalid
        copy_add_item = add_item.copy()
        del copy_add_item['id']
        response = client.post('/items', json = copy_add_item)          
        assert response.status_code == 400
        # print(f'✅ Status code is 400 when {key} is missing')
        assert response.is_json
        assert response.get_json()['Error'] == 'Invalid payload structure, key names missed'

    # check for conflicts - duplicate items
    response = client.post('/items', json = add_item)
    assert response.status_code == 409
    assert response.is_json
    assert response.get_json()['Error'] == 'The id: 3 already exists, insert a different id'


def test_update_item(client: FlaskClient):
    update_item: dict[str, str] = {
        'name': '<Updated> Item 1', 
        'description': 'This is updated item 1'
    }
    response = client.put('/items/1', json = update_item)
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json()['item']['name'] == '<Updated> Item 1'

    response = client.put('/items/999', json = update_item)
    assert response.status_code == 404
    assert response.is_json
    assert response.get_json()['Error'] == 'Item: 999 not found'


def test_delete_item(client: FlaskClient):
    response = client.delete('/items/1')
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json()['message'] == 'item successfully deleted'

    """
    1. This might seem counterintuitive since the item '999' does not exist, but it could be that the API is designed to return 200 even if the item was not found, to avoid leaking information about the existence of items.
    2. Graceful Handling of Non-Existent Items: The test ensures that the API handles requests to delete non-existent items without errors and returns a consistent response.
    3. Prevent Information Leakage: By returning a 200 status code and a generic message, the API avoids revealing whether the item existed or not, which can be a security measure.
    """
    response = client.delete('/items/999')
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json()['message'] == 'item successfully deleted'

