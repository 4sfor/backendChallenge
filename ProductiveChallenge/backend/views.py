# from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .permission import IsOwnerOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import *


# Create your views here.


class GlobalChallengeView(mixins.ListModelMixin,
                          GenericViewSet):
    queryset = GlobalChallenge.objects.all()
    serializer_class = GlobalChallengeSerializer


class UserChallengeView(APIView):

    def get(self, request, format=None):
        challenges = UserChallenge.objects.filter(owner=request.user)
        serializer = UserChallengeSerializer(challenges, many=True)
        return Response(serializer.data)


    # def post(self,request,format=None):
    #     user = request.user
    #     serializer = UserChallengeSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AchievementView(mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


#?
class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserInformationView(APIView):
    def get(self, request, format=None):
        user = request.user
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)

    def put(self, request, format=None):
        user = request.user
        serializer = UserInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserGlobalChallengeView(APIView):
    def get(self, request, format=None):
        user = UsersGlobalChallenge.objects.filter(owner=request.user)
        serializer = UserGlobalChallengeSerializer(user, many=True)
        return Response(serializer.data)




class Logout(APIView):
    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
