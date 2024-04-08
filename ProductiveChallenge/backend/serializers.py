from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChallenge
        fields = ('title', 'description', 'user')



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'description')



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',  'article_id', 'author_id')
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
    class Meta:
        model = UsersGlobalChallenge
        fields = ('completed', 'global_challenge_id', 'user_id')



class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

