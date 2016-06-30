from __future__ import unicode_literals

from django.db import models
from photologue.models import Photo


class Article(models.Model):
    slug = models.CharField(max_length=512, blank=True, null=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    image = models.ForeignKey(Photo, related_name='articles', blank=True, null=True)
    authors = models.ManyToManyField('company.Employee', blank=True)
    keywords = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title
