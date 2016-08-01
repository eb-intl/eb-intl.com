# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20160628_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='photologue.Photo'),
        ),
    ]
