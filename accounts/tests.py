from django.test import TestCase
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_user_signup(client):
    data = {
        "username": "testuser",
        "password": "testpassword",
        "nickname": "TestNick",
    }

    response = client.post("/accounts/signup/", data, content_type="application/json")
    
    assert response.status_code == 201
    assert response.data["username"] == "testuser"
    assert response.data["nickname"] == "TestNick"
