# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u5e8f\u53f7')),
                ('name', models.CharField(max_length=32, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('port', models.IntegerField(verbose_name='PORT')),
                ('business', models.CharField(max_length=32, verbose_name='\u4e1a\u52a1\u7ebf')),
                ('area', models.CharField(max_length=32, verbose_name='\u533a\u57df')),
                ('in_date', models.DateTimeField(verbose_name='\u5165\u5e93\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='\u7528\u6237\u540d')),
                ('passwd', models.CharField(max_length=255, verbose_name='\u5bc6\u7801')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.User', to_field='name', verbose_name='\u5c5e\u4e3b'),
        ),
    ]
