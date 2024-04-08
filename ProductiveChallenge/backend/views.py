# from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *


# Create your views here.


class GlobalChallengeView(viewsets.ModelViewSet):
    queryset = GlobalChallenge.objects.all()
    serializer_class = GlobalChallengeSerializer




class UserChallengeView(viewsets.ModelViewSet):
    queryset = UserChallenge.objects.all()
    serializer_class = UserChallengeSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AchievementView(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserInformationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer


class UserGlobalChallengeView(viewsets.ModelViewSet):
    queryset = UsersGlobalChallenge.objects.all()
    serializer_class = UserGlobalChallengeSerializer
