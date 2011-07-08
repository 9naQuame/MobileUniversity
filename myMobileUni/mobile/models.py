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

class Course(models.Model):
	code = models.CharField(max_length = 10)
	name = models.CharField(max_length = 40)
	abbreviation = models.CharField(max_length = 10)
	def __unicode__(self):
		return self.name

class Timetable(models.Model):
	examVenue = models.CharField(max_length = 10)
	examTime = models.DateField()
	lectureVenue = models.CharField(max_length = 10)
	lectureTime = models.DateField()
	semester = models.IntegerField()
	year = models.IntegerField()
	code = models.ForeignKey(Course)
	major = models.ForeignKey(Major)
	def __unicode__(self):
		return self.code

class Major(models.Model):
	faculty = models.CharField(max_length = 60)
	department = models.CharField(max_length = 60)
	majors = models.CharField(max_length = 60)
	def __unicode__(self):
		return self.majors

