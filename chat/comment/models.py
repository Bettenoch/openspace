# chat/comment/models.py
from django.db import models
from chat.abstract.models import AbstractManager, AbstractModel


class CommentManager(AbstractManager):
    pass


class Comment(AbstractModel):
    post = models.ForeignKey("chat_post.Post", on_delete=models.PROTECT)
    author = models.ForeignKey("chat_user.User", on_delete=models.PROTECT)
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return self.author.name
