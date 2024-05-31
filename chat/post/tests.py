import pytest
from chat.fixtures.user import user
from chat.post.models import Post


# Create your tests here.
@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(author=user, body="Should be  a post")
    assert post.author == user
    assert post.body == "Should be  a post"
