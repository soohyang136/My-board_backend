from django.contrib import admin
from django.contrib.auth.models import User
from .models import Board, Comment

admin.site.register(Board)
admin.site.register(Comment)

# Register your models here.
