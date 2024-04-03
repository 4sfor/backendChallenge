from django.urls import path
from .views import *

urlpatterns = [
    path('/global-challenge', GlobalChallenge.as_view()),
    path('/article', Article.as_view()),
    path('/acivement', Achievement.as_view()),
    path('/user-chalange', UserChallenge.as_view()),
    path('/comment', Comment.as_view()),
    path('/user-info', UserInformation.as_view()),
    path('/user-global-challenge', UserGlobalChallenge.as_view())
]