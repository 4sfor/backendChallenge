from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChallenge
        fields = ()
        pass


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ()
        pass


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ()
        pass


class GlobalChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalChallenge
        fields = ()
        pass


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ()
        pass


class UserGlobalChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersGlobalChallenge
        fields = ()
        pass


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ()
        pass
