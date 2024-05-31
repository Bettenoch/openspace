import pytest

from chat.fixtures.user import user
from chat.fixtures.post import post
from chat.comment.models import Comment

@pytest.mark.django_db
def test_comment(user, post):
    comment = Comment.objects.create(
        post=post,
        author=user,
        body="This is a test comment"
    )
    assert comment.post == post
    assert comment.author == user
    assert comment.body == "This is a test comment"
    assert comment.edited == False