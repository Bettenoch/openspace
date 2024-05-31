import pytest
from chat.user.models import User


# Create your tests here.
data_user = {
    "username": "kingpin",
    "email": "kingpin24@gmail.com",
    "password": "kingpin24",
    "first_name": "king",
    "last_name": "Pin",
    "bio": "kingpin",
}

data_superuser = {
    "username": "test_superuser",
    "email": "testsuperuser@gmail.com",
    "first_name": "Bett",
    "last_name": "superuser",
    "password": "super254"
}

@pytest.mark.django_db

def test_create_user():
    user = User.objects.create(**data_user)
    assert user.username == data_user["username"]
    assert user.email == "kingpin24@gmail.com"
    assert user.password == "kingpin24"
    assert user.first_name == "king"
    assert user.last_name == "Pin"
    assert user.bio == "kingpin"
    
@pytest.mark.django_db

def test_create_superuser():
    user = User.objects.create_superuser(**data_superuser)
    assert user.username == data_superuser["username"]
    assert user.email == "testsuperuser@gmail.com"
    assert user.first_name == "Bett"
    assert user.last_name == "superuser"
    assert user.is_superuser == True
    assert user.is_staff == True
    assert user.is_active == True