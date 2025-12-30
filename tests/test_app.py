import pytest
import sys
import os

# Add parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == 'Welcome to Flask App'
    assert response.json['status'] == 'success'

def test_health_route(client):
    """Test the health check route"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'