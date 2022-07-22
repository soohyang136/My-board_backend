from . import views
from django.urls import path

urlpatterns = [
    path('join/', views.join, name='join'),
    path('login/', views.login, name='login'),
]