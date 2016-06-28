from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import Site
from fontawesome.fields import IconField
from photologue.models import Photo


class Service(models.Model):
    sites = models.ManyToManyField(Site)
    slug = models.CharField(max_length=512, blank=True, null=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='services')
    icon = IconField()

    def __unicode__(self):
        return self.title
