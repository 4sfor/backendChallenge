from django.urls import path, include
from .views import *
from .routers import *
from rest_framework.authtoken import views

urlpatterns = [
    path('', include(routerArticle.urls)),
    path('', include(routerGlobalChallenge.urls)),
    path('', include(routerAchievement.urls)),
    path('user-challenge/', UserChallengeView.as_view()),
    path('', include(routerComment.urls)),
    path('user-info/', UserInformationView.as_view()),
    path('user-global-challenge/', UserGlobalChallengeView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('logout/',Logout.as_view())
]