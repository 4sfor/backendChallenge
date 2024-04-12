# from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .permission import IsOwnerOrReadOnly

from .serializers import *


# Create your views here.


class GlobalChallengeView(mixins.ListModelMixin,
                   GenericViewSet):


    queryset = GlobalChallenge.objects.all()
    serializer_class = GlobalChallengeSerializer
    permission_classes = [IsAuthenticated]




class UserChallengeView(viewsets.ModelViewSet):
    queryset = UserChallenge.objects.all()
    serializer_class = UserChallengeSerializer
    permission_classes = [IsOwnerOrReadOnly]





class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class AchievementView(mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]


#?
class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class UserInformationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = []#?


class UserGlobalChallengeView(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = UsersGlobalChallenge.objects.all()
    serializer_class = UserGlobalChallengeSerializer
    permission_classes = [IsOwnerOrReadOnly]
