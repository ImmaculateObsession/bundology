from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Content(models.Model):
    title = models.CharField(max_length=140)
    creator = models.ForeignKey(User)
    content = models.TextField()
    changed = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class Bundle(models.Model):
    title = models.CharField(max_length=140)
    creator = models.ForeignKey(User)
    items = models.ManyToManyField('Content')
    changed = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title