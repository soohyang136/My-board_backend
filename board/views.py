from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, BoardSerializer
from rest_framework import status
from django.contrib.auth import authenticate
import jwt
from django.conf import settings
from django.contrib.auth.models import User
from .models import Board

@api_view(['POST'])
def join(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    print(request.data)
    username = request.data["username"]
    password = request.data["password"]
    if not username or not password:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user is not None:
        encode_jwt = jwt.encode({"id": user.pk}, settings.SECRET_KEY, algorithm="HS256")
        response = Response()
        response.data = {"token": encode_jwt}
        return response
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def uesrview(request):
    token = request.GET['token']
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    user = User.objects.get(id=payload['id'])
    serializer = UserSerializer(user)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def getBoard(request):
    board = Board.objects.all()
    boardlist = []
    for i in board:
        serializer = BoardSerializer(i)
        author = User.objects.get(id=serializer.data['author'])
        boards = {'id': serializer.data['id'], 'title': serializer.data['title'], 'author': author.username, 'created_at': serializer.data['created_at']}
        boardlist.append(boards)
    return Response(boardlist)