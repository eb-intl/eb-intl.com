from __future__ import unicode_literals

from django.db import models

from photologue.models import  Photo


class Product(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Photo, related_name='client')
    private = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

