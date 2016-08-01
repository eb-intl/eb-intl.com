# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('ours', 'Our Products'), ('client', 'Client Products')], max_length=512, null=True)),
                ('slug', models.CharField(blank=True, max_length=512, null=True)),
                ('model', models.CharField(blank=True, max_length=512, null=True)),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('public', models.BooleanField(default=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='photologue.Photo')),
                ('images', models.ManyToManyField(blank=True, related_name='products', to='photologue.Photo')),
            ],
        ),
    ]