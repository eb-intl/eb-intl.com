from __future__ import unicode_literals

from django.db import models
from photologue.models import ImageModel, Photo

from apps.products import Product


class Client(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=512, blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='client')
    private = models.BooleanField(default=True)
    products = models.ManyToManyField(
        Product, related_name='clients', blank=True)

    def __unicode__(self):
        return self.name
