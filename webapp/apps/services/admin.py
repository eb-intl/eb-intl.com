# -*- coding: utf-8 -*-
"""
"""
from django.contrib import admin

from models import Service, ServiceGroup


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'slug', 'description', 'text')
    ordering = ['id', 'title', 'slug', 'description']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ServiceGroup)
class ServiceGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')
    ordering = ['id', 'title', 'description']
    list_display_links = ('id', 'title')

