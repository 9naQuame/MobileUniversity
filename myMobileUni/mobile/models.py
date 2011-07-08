from django.db import models
from django.contrib import admin

class event(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	venue = models.TextField()
	time = models.DateTimeField(auto_now_add=True)
	rate = models.DecimalField(max_digits=10, decimal_places=2)
	organisers = models.TextField()
	approval = models.TextField()
	eventtype = models.TextField()
	status = models.CharField(max_length=10)
	def __unicode__(self):
		return self.title

class news(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)
	author = models.CharField(max_length=50)
	def __unicode__(self):
		return self.title

class announcement(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.title

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


class Faculty(models.Model):
	name = models.CharField(max_length = 60)
	yearCreated = models.IntegerField()
	def __unicode__(self):
		return self.name

class department(models.Model):
	name = models.CharField(max_length = 60)
	faculty = models.ForeignKey(Faculty)
	def __unicode__(self):
		return self.name

class Course(models.Model):
	code = models.CharField(max_length = 10)
	name = models.CharField(max_length = 40)
	abbreviation = models.CharField(max_length = 10)
	department = models.ForeignKey(department)
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
	def __unicode__(self):
		return self.code

admin.site.register(Picture)
admin.site.register(Emergency)
admin.site.register(Calendar)
admin.site.register(Course)
admin.site.register(Timetable)
admin.site.register(Faculty)
admin.site.register(department)



