from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='版块名称')
    description = models.CharField(max_length=100, verbose_name='描述信息')

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255, verbose_name='主题')
    last_updated = models.DateTimeField(auto_now_add=True, verbose_name='最后更新时间')
    board = models.ForeignKey(Board, related_name='topics', verbose_name='版块名称', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', verbose_name='发布者',on_delete=models.CASCADE)


class Post(models.Model):
    message = models.TextField(max_length=40000, verbose_name='内容')
    topic = models.ForeignKey(Topic, related_name='posts', verbose_name='发布主题', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, verbose_name='主题创建时间')
    updated_at = models.DateTimeField(null=True, verbose_name='主题更新时间')
    created_by = models.ForeignKey(User, related_name='posts', verbose_name='创建时间', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', verbose_name='更新时间', on_delete=models.CASCADE)
