from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from chat.abstract.models import AbstractManager, AbstractModel
class UserManager(BaseUserManager, AbstractManager):
    def create_user(self, username, email, password=None, **kwargs):
        """create a new user with the given username and email"""
        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users must have an email address')
        if password is None:
            raise TypeError('Users must have a password')

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **kwargs):
        if password is None:
            raise TypeError('Superusers must have a password')
        if email is None:
            raise TypeError('Superusers must have an email address')
        if username is None:
            raise TypeError('Superusers must have a username')

        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,AbstractModel, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, max_length=255, unique=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    posts_liked = models.ManyToManyField("chat_post.Post", related_name="liked_by")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    def like(self, post):
        return self.posts_liked.add(post)

    def remove_like(self, post):
        return self.posts_liked.remove(post)
    
    def has_liked(self, post):
        return self.posts_liked.filter(pk=post.pk).exists()
