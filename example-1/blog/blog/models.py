from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)


class Comment(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    text = models.CharField(max_length=5000)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    comment_type = models.ChoiceField(['question', 'comment'])
