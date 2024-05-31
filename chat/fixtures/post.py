import pytest

from chat.fixtures.user import user
from chat.post.models import Post


@pytest.fixture
def post(db, user):
    return Post.objects.create(
        author=user,
        body="test post",
    )
