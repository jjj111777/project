from django.test import TestCase
import pytest
from django.contrib.auth import get_user_model

#회원가입 테스트 코드
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


# 로그인 테스트 코드
@pytest.mark.django_db
def test_user_login(client):
    user = User.objects.create_user(username="testuser", password="testpassword")

    data = {
        "username": "testuser",
        "password": "testpassword",
    }

    response = client.post("/accounts/login/", data, content_type="application/json")

    assert response.status_code == 200
    assert "token" in response.data  # 응답에 토큰이 포함되어 있어야 함