from . import views
from django.urls import path

urlpatterns = [
    path('join/', views.join, name='join'),
    path('login/', views.login, name='login'),
    path('userview/', views.uesrview, name='userview'),
    path('getBoard/', views.getBoard, name='getboard'),
]