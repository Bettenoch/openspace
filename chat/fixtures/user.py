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

@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**data_user)