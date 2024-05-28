from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserChallengeSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault(),write_only=True)
    owner_info = serializers.SerializerMethodField()

    class Meta:
        model = UserChallenge
        fields = ( 'owner_info', 'owner','title', 'description')
        read_only_fields = ('owner_info',)

    def get_owner_info(self, obj):
        return LimitedUserSerializer(obj.owner).data



class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class LimitedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault(), write_only=True)
    owner_detail = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('title', 'description', 'owner', 'owner_detail',)
        read_only_fields = ('valution', 'published', 'owner_detail')

    def get_owner_detail(self, obj):
        return LimitedUserSerializer(obj.owner).data


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault(), write_only=True)
    owner_detail = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('content', 'article', 'owner', 'owner_detail')
        read_only_fields = ('published', 'owner_detail')

    def get_owner_detail(self, obj):
        return LimitedUserSerializer(obj.owner).data


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatGlobalChallenge
        fields = ('title',)


class GlobalChallengeSerializer(serializers.ModelSerializer):
    cat = serializers.SerializerMethodField()

    class Meta:
        model = GlobalChallenge
        fields = ('id','title', 'description', 'cat', 'time_start', 'time_end')

    def get_cat(self, obj):
        return CatSerializer(obj.cat).data


class AchievementSerializer(serializers.ModelSerializer):
    global_challenge = serializers.SerializerMethodField()

    class Meta:
        model = Achievement
        fields = ('title',  'global_challenge')

    def get_global_challenge(self, obj):
        return GlobalChallengeSerializer(obj.global_challenge).data


class UserGlobalChallengeSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    global_challenge_detail = serializers.SerializerMethodField()

    class Meta:
        model = UsersGlobalChallenge
        fields = ('completed',  'global_challenge','global_challenge_detail', 'owner')
        read_only_fields = ('global_challenge_detail',)

    def get_global_challenge_detail(self, obj):
        return GlobalChallengeSerializer(obj.global_challenge).data