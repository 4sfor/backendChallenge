from rest_framework import routers
from .views import *

routerArticle = routers.SimpleRouter()
routerArticle.register(r'article', ArticleView)

routerGlobalChallenge = routers.SimpleRouter()
routerGlobalChallenge.register(r'global-challenge', GlobalChallengeView)

routerAchievement = routers.SimpleRouter()
routerAchievement.register(r'achievement', AchievementView)

routerUserChallenge = routers.SimpleRouter()
routerUserChallenge.register(r'user-challenge', UserChallengeView)

routerComment = routers.SimpleRouter()
routerComment.register(r'comment', CommentView)

routerUserInfo = routers.SimpleRouter()
routerUserInfo.register(r'user-info', UserInformationView)

routerUserGlobalChallenge = routers.SimpleRouter()
routerUserGlobalChallenge.register(r'user-global-challenge', UserGlobalChallengeView)
