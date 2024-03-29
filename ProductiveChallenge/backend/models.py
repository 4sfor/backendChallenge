from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserChallenges(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')

    class Meta:
        verbose_name = 'Челледж пользователя'
        verbose_name_plural = 'Челленджи пользователя'


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='описание')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    autor = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    valuation = models.FloatField(verbose_name='Оценка')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published']


class Comments(models.Model):
    content = models.TextField(verbose_name='Содержание')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-published']


class GlobalChallenges(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    time_start = models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')
    time_end = models.DateTimeField(auto_now_add=False, verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'Глобальный челлендж'
        verbose_name_plural = 'Глобальные челленджи'
        ordering = ['-time_start']


class Achievements(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    global_challenge = models.ForeignKey(GlobalChallenges, on_delete=models.CASCADE, verbose_name='Глобальный Челлендж')

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class UsersGlobalChallenges(models.Model):
    global_challenge = models.ForeignKey(GlobalChallenges, on_delete=models.CASCADE, verbose_name='Глобальный челлендж')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    completed = models.BooleanField(default=False, verbose_name='Выполнено')

    class Meta:
        verbose_name = 'Пользователи учавствующие в глобальный челленджах'
