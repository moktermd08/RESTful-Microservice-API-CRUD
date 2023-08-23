import json
from app import create_app

app = create_app()

def test_create_user():
    client = app.test_client()
    response = client.post('/users', json={'id': '1', 'name': 'John'})
    assert response.status_code == 201
    assert json.loads(response.data) == {"message": "User created successfully"}

# Add more tests for read, update, and delete
