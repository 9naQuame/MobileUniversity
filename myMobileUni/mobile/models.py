from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Event(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	venue = models.CharField(max_length=15)
	time = models.TimeField()
	date = models.DateField()
	rate = models.DecimalField(max_digits=10, decimal_places=2)
	organisers = models.CharField(max_length=20)
	approval = models.CharField(max_length=10)
	eventtype = models.CharField(max_length=10)
	status = models.CharField(max_length=10)
	def __unicode__(self):
		return self.title

class EventAdmin(admin.ModelAdmin):
	list_display = ('title','organisers','venue','date','time')
	search_fields = ('title','body')
	list_filter = ('date',)

class New(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)
	author = models.CharField(max_length=50)
	def __unicode__(self):
		return self.title

class NewAdmin(admin.ModelAdmin):
	list_display = ('title','created','updated')
	search_fields = ('title','body')
	list_filter = ('created',)

class Announcement(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.title

class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ('title','created','updated')
	search_fields = ('title','body')
	list_filter = ('created',)

class Picture(models.Model):
	name = models.CharField(max_length=15)
	image = models.FileField(upload_to="static")
	description = models.TextField()
	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)
	def __unicode__(self):
		return self.name

class PictureAdmin(admin.ModelAdmin):
	list_display = ('name','description','created','updated')
	search_fields = ('name',)

class Emergency(models.Model):
	name = models.CharField(max_length=60)
	number = models.IntegerField()
	location = models.TextField()
	def __unicode__(self):
		return self.name

class EmergencyAdmin(admin.ModelAdmin):
	search_fields = ('name',)
	list_display = ('name','number','location')

class Calendar(models.Model):
	datetime = models.DateTimeField()
	year = models.IntegerField()
	event = models.TextField()
	semester = models.IntegerField()
	def __unicode__(self):
		return self.year

class CalendarAdmin(admin.ModelAdmin):
	list_display = ('datetime','event','year','semester')
	search_fields = ('datetime',)

class Faculty(models.Model):
	name = models.CharField(max_length = 60)
	yearCreated = models.IntegerField()
	def __unicode__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length = 60)
	faculty = models.ForeignKey(Faculty)
	def __unicode__(self):
		return self.name

class Course(models.Model):
	code = models.CharField(max_length = 10) #i.e. CS.157
	name = models.CharField(max_length = 40) # Computer Organ.....
	abbreviation = models.CharField(max_length = 10) # i.e. COA
	lectureVenue = models.CharField(max_length = 60)#location
	lectureDay = models.CharField(max_length = 60) # 'monday, wednesday, friday'
	lectureStart = models.CharField(max_length = 9) #todo make this a time
	lectureEnd = models.CharField(max_length = 9) #todo make this a time
	semester = models.IntegerField() #only 1 or 2
	year = models.IntegerField()#length of exactly 4

	department = models.ForeignKey(Department)
	def __unicode__(self):
		return self.name

class Exam(models.Model):
	examVenue = models.CharField(max_length = 10)
	examDate= models.DateField()
	examStart=models.TimeField()
	examEnd = models.TimeField()
	
	# course = models.ForeignKey(Course) # todo decide if you need a course details page
	department = models.ForeignKey(Department)
	def __unicode__(self):
		return self.code

admin.site.register(Picture,PictureAdmin)
admin.site.register(Emergency,EmergencyAdmin)
admin.site.register(Calendar,CalendarAdmin)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Announcement,AnnouncementAdmin)
admin.site.register(New,NewAdmin)
admin.site.register(Event,EventAdmin)



