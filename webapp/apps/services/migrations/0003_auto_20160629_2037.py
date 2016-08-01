# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20160629_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='photologue.Photo'),
        ),
    ]