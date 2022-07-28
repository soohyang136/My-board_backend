from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.CharField(max_length=1000)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    created_at = models.CharField(max_length=1000)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, default=None)
