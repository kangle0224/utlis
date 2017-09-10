# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Asset(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=32, verbose_name='主机名')
    ip = models.GenericIPAddressField(verbose_name='IP')
    port = models.IntegerField(verbose_name='PORT')
    owner = models.ForeignKey(to='User', to_field='name', verbose_name='属主')
    business = models.CharField(max_length=32, verbose_name='业务线')
    area = models.CharField(max_length=32, verbose_name='区域')
    in_date = models.DateTimeField(verbose_name='入库时间')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class User(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='用户名')
    passwd = models.CharField(max_length=255, verbose_name='密码')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

