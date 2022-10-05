from django.contrib.auth.models import User
from django.db import models


class UrlService(models.Model):
    url_all = models.TextField(verbose_name='Введите ссылку')
    url_short = models.CharField(max_length=40) #добавить  юник для отсутствия повторяемости
    username = models.ForeignKey(User, on_delete=models.CASCADE)

