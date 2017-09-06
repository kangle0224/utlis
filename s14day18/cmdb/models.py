# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=32, verbose_name="用户类型")

class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name="用户名")
    pwd = models.CharField(max_length=32, verbose_name="密码")
    email = models.CharField(max_length=32, verbose_name="邮箱")
    type = models.ForeignKey(UserType, verbose_name="用户类型")
