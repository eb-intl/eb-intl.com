# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 01:04
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
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('slug', models.CharField(blank=True, max_length=512, null=True)),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='photologue.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=512, null=True)),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('primary', models.BooleanField(default=False)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offices', to='photologue.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='company.Position'),
        ),
    ]
