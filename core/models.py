from django.contrib.auth.models import User
from django.db import models


class Type(models.Model):
    value = models.CharField(max_length=200)

    def __unicode__(self):
        return self.value


class Track(models.Model):
    track_type = models.ForeignKey(Type)
    title = models.CharField(max_length=200)
    minutes = models.IntegerField(default=0)
    place = models.CharField(max_length=200)
    date = models.DateTimeField('tracking date')
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return "%s: %s (%s min) - %s" % (self.track_type,
                                         self.title,
                                         self.minutes,
                                         self.created_by)
