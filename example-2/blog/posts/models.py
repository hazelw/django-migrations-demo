from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    text = models.CharField(max_length=5000)
    sentiment = models.CharField(
        choices=[('positive', 'positive'), ('neutral', 'neutral'), ('negative', 'negative')],
        max_length=10
    )
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    comment_type = models.CharField(
        choices=[('question', 'question'), ('comment', 'comment')],
        max_length=10
    )
