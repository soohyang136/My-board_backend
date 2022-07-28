from datetime import datetime

import pytz
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, BoardSerializer, UserviewSerializer, CommentSerializer
from rest_framework import status
from django.contrib.auth import authenticate
import jwt
from django.conf import settings
from django.contrib.auth.models import User
from .models import Board, Comment

@api_view(['POST'])
def join(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
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
    serializer = UserviewSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def getBoards(request):
    board = Board.objects.all()
    boardlist = []
    for i in board:
        serializer = BoardSerializer(i)
        author = User.objects.get(id=serializer.data['author'])
        boards = {'id': serializer.data['id'], 'title': serializer.data['title'], 'author': author.username, 'created_at': serializer.data['created_at']}
        boardlist.append(boards)
    return Response(boardlist)

@api_view(['POST'])
def registerBoard(request):
    form = request.data
    now = pytz.timezone('Asia/Seoul')
    now = datetime.now(now)
    day = str(now)[:10]
    time = str(now.time())[:8]
    created = day + " " + time
    form["created_at"] = created
    serializer = BoardSerializer(data=form)
    if serializer.is_valid():
        serializer.save()
        return Response("등록성공")
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getBoard(request):
    board = Board.objects.get(id=request.GET['id'])
    serializer = BoardSerializer(board)
    author = User.objects.get(id=serializer.data['author'])
    reboard = {'id': serializer.data['id'], 'title': serializer.data['title'], 'content': serializer.data['content'], 'author': author.username, 'created_at': serializer.data['created_at']}
    return Response(reboard)

@api_view(['POST'])
def registerComment(request):
    form = request.data
    now = pytz.timezone('Asia/Seoul')
    now = datetime.now(now)
    day = str(now)[:10]
    time = str(now.time())[:8]
    created = day + " " + time
    form["created_at"] = created
    serializer = CommentSerializer(data=form)
    if serializer.is_valid():
        serializer.save()
        return Response("등록성공")
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getComments(request):
    comments = Comment.objects.filter(board=request.GET['id'])
    recomment = []
    for i in comments:
        serializer = CommentSerializer(i)
        author = User.objects.get(id=serializer.data['author'])
        re_Comment = {'id': serializer.data['id'], 'content': serializer.data['content'], 'author': author.username, 'created_at': serializer.data['created_at']}
        recomment.append(re_Comment)
    return Response(recomment)
