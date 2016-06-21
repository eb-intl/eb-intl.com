from __future__ import unicode_literals

from django.db import models

from photologue.models import ImageModel, Photo


class Position(models.Model):
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    position = models.ForeignKey(Position, related_name='employees')
    image = models.ForeignKey(Photo, related_name='person')

    def __unicode__(self):
        return self.name


class Office(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    #location =
    image = models.ForeignKey(Photo, related_name='person')

    def __unicode__(self):
        return self.name
