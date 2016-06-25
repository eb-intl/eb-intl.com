from __future__ import unicode_literals

from django.db import models

from photologue.models import Photo


class ServiceItem(models.Model):
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=512, blank=True, null=True)
    icon = models.CharField(max_length=512, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Service(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=512, blank=True, null=True)
    icon = models.CharField(max_length=512, blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='services')
    items = models.ManyToManyField(ServiceItem, related_name='services', blank=True)

    def __unicode__(self):
        return self.title
