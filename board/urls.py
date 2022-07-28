from . import views
from django.urls import path

urlpatterns = [
    path('join/', views.join, name='join'),
    path('login/', views.login, name='login'),
    path('userview/', views.uesrview, name='userview'),
    path('getBoards/', views.getBoards, name='getBoards'),
    path('registerBoard/', views.registerBoard, name='registerBoard'),
    path('getBoard/', views.getBoard, name='getBoard'),
    path('registerComment/', views.registerComment, name='registerComment'),
    path('getComments/', views.getComments, name='getComments'),
]