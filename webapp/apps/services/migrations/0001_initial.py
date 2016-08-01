# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import fontawesome.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=512, null=True)),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('icon', fontawesome.fields.IconField(blank=True, max_length=60)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='photologue.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_groups', to='photologue.Photo')),
                ('services', models.ManyToManyField(related_name='groups', to='services.Service')),
            ],
        ),
    ]