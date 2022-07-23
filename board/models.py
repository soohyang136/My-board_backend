from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
