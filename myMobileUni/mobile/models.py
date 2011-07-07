from django.db import models
from django.contrib import admin

class Picture(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    created = models.DateField()
    updated = models.DateField()
    def __unicode__(self):
        return self.name

class Emergency(models.Model):
    name = models.CharField(max_length=60)
    number = models.IntegerField()
    location = models.TextField()
    def __unicode__(self):
	return self.name

class Calendar(models.Model):
    datetime = models.DateTimeField()
    event = models.TextField()
    semester = models.IntegerField()
    def __unicode__(self):
	return self.event
