from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import Site
from fontawesome.fields import IconField
from photologue.models import Photo


class Service(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='services', blank=True, null=True)
    icon = IconField()

    def __unicode__(self):
        return self.title

class ServiceGroup(models.Model):
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='service_groups', blank=True, null=True)
    services = models.ManyToManyField(Service, related_name='groups', blank=True)

    def __unicode__(self):
        return self.title
