from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserChallenge(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')

    class Meta:
        verbose_name = 'Челледж пользователя'
        verbose_name_plural = 'Челленджи пользователя'


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='описание')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')
    valuation = models.FloatField(verbose_name='Оценка', default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published']


class Comment(models.Model):
    content = models.TextField(verbose_name='Содержание')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-published']


class CatGlobalChallenge(models.Model):
    title = models.CharField(max_length=50, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория челленждей"
        verbose_name_plural = "Категории челледжей"

class GlobalChallenge(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    cat = models.ForeignKey(CatGlobalChallenge, on_delete=models.PROTECT, verbose_name='Категория')
    time_start = models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')
    time_end = models.DateTimeField(auto_now_add=False, verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'Глобальный челлендж'
        verbose_name_plural = 'Глобальные челленджи'
        ordering = ['-time_start']





class Achievement(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    global_challenge = models.ForeignKey(GlobalChallenge, on_delete=models.CASCADE, verbose_name='Глобальный Челлендж')

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class UsersGlobalChallenge(models.Model):
    global_challenge = models.ForeignKey(GlobalChallenge, on_delete=models.CASCADE, verbose_name='Глобальный челлендж')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    completed = models.BooleanField(default=False, verbose_name='Выполнено')

    class Meta:
        verbose_name = 'Пользователи учавствующие в глобальный челленджах'


class Stats(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    challenge_completed = models.IntegerField(default=0, verbose_name='Челленждей выполнено')
    challenge_plans = models.IntegerField(default=0, verbose_name='Челленждей запланировано')
    challenge_active = models.IntegerField(default=0, verbose_name='Челленждей запланировано')
    friends = models.IntegerField(default=0, verbose_name='Количесвто друзей')
    achievements_received =models.IntegerField(default=0, verbose_name='Получения достижений')
    challenge_created = models.IntegerField(default=0, verbose_name='Челлeнджей создано')

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'


class Support(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    title = models.CharField(max_length=30, verbose_name='Тайтл')
    description = models.TextField(verbose_name='Описание')
    solved = models.BooleanField(default=False, verbose_name='Решено')

    class Meta:
        verbose_name = 'Поддержка'
        verbose_name_plural ='Поддержка'


class UserConf(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    conf = models.BooleanField(default=True, verbose_name='Закрытый аккаунт')
    #img

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
