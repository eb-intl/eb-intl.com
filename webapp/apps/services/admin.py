# -*- coding: utf-8 -*-
"""
"""
from django.contrib import admin

from models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'slug', 'description')
    ordering = ['id', 'title', 'slug', 'description']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}

