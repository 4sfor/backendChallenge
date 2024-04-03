# from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.


class GlobalChallenge(generics.ListAPIView):
    queryset = None


class UserChallenge(generics.ListAPIView):
    pass


class Comment(generics.ListAPIView):
    queryset = None


class Achievement(generics.ListAPIView):
    queryset = None


class Article(generics.ListAPIView):
    queryset = None


class UserInformation(generics.ListAPIView):
    queryset = None


class UserGlobalChallenge(generics.ListAPIView):
    queryset = None
