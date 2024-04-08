from django.urls import path, include
from .views import *
from .routers import *

urlpatterns = [
    path('', include(routerArticle.urls)),
    path('', include(routerGlobalChallenge.urls)),
    path('', include(routerAchievement.urls)),
    path('', include(routerUserChallenge.urls)),
    path('', include(routerComment.urls)),
    path('', include(routerUserInfo.urls)),
    path('', include(routerUserGlobalChallenge.urls)),
]