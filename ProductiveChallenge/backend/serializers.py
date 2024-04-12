from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserChallengeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserChallenge
        fields =('user', 'title', 'description')


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Article
        fields = ('title', 'description', 'author')
        read_only_fields = ('valution', 'published')



class CommentSerializer(serializers.ModelSerializer):
    author= serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = ('content',  'article_id', 'author')
        read_only_fields = ('published',)



class GlobalChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalChallenge
        fields = ('title', 'description', 'time_start', 'time_end')



class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('title', 'global_challenge_id')



class UserGlobalChallengeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UsersGlobalChallenge
        fields = ('completed', 'global_challenge_id', 'user')



class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

