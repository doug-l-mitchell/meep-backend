import pytest

from src.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User('evan@aol.com')
    return user
