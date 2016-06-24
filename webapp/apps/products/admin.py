# -*- coding: utf-8 -*-
"""
"""
from django.contrib import admin

from models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'private')
    search_fields = ('id', 'name', 'slug', 'description')
    ordering = ['id', 'name', 'slug', 'description', 'private']
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
