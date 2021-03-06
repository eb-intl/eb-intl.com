# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('slug', models.CharField(blank=True, max_length=512, null=True)),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('publish', models.BooleanField(default=False)),
                ('keywords', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
