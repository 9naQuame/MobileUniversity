from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import New, Event, Announcement, Faculty, Department,Course, Exam, Emergency, Picture, Calendar
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

def news_list(request, limit=60):
	news_list = New.objects.all()
	t = loader.get_template('mobile/newslist.html')
	c = Context({'news_list':news_list})
	return HttpResponse(t.render(c))

def announcement_list(request, limit=120):
	announcement_list = Announcement.objects.all()
	t = loader.get_template('mobile/announcementlist.html')
	c = Context({'announcement_list':announcement_list})
	return HttpResponse(t.render(c))

def event_list(request, limit=60):
	event_list = Event.objects.all()
	t = loader.get_template('mobile/eventlist.html')
	c = Context({'event_list':event_list})
	return HttpResponse(t.render(c))

def news_detail(request, id):
	news = New.objects.get(pk=id)
	t = loader.get_template('mobile/newsdetail.html')
	c = Context({'news':news})
	return HttpResponse(t.render(c))

def event_detail(request, id):
	events = Event.objects.get(pk=id)
	t = loader.get_template('mobile/eventdetail.html')
	c = Context({'events':events})
	return HttpResponse(t.render(c))

class SearchForm(forms.Form):
	search = forms.CharField()

class EventForm(ModelForm):
	date = forms.DateField(widget=SelectDateWidget())
	body = forms.CharField(widget=forms.Textarea(attrs={'class':'eventBody'}))
	#time = forms.TimeField(widget=SelectTimeWidget())
	class Meta:
		model = Event
		exclude = ['eventtype','status']

@csrf_exempt
def add_event(request):
	if request.method == 'POST':
		event = Event(eventtype = 'Unofficial', status ='Holds')
		form = EventForm(request.POST,instance=event)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/mobile/eventlist')
	else:
		form = EventForm()
	t = loader.get_template('mobile/eventadd.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))

#Lady-Asaph
#faculty list
def faculty_list(request, limit=100):
	faculty_list = Faculty.objects.all()
	print faculty_list
	t = loader.get_template('mobile/faculty.html')
	c = Context({'faculty':faculty_list})
	return HttpResponse(t.render(c))


def faculty_department(request, id, limit=100):
	faculty_list = Faculty.objects.get(pk=id)
	department_list = Department.objects.filter(faculty__id=id)
	t = loader.get_template('mobile/department.html')
	c = Context({'faculty':faculty_list, 'department':department_list})
	return HttpResponse(t.render(c))

def course_department(request, id, limit=100):
	department_list = Department.objects.get(pk=id)
	course_list = Course.objects.filter(department__id = id)
	t = loader.get_template('mobile/course.html')
	c = Context({'department':department_list, 'course':course_list})
	return HttpResponse(t.render(c))

def classschedule(request, id, limit=100):
	department_list = Department.objects.get(pk=id)
	course_list = Course.objects.filter(department__id = id)
	t = loader.get_template('mobile/classschedule.html')
	c = Context({'department':department_list, 'course':course_list})
	return HttpResponse(t.render(c))

def coursedetial(request, id, limit = 100):
	course_list = Course.objects.filter(pk = id)
	t = loader.get_template('mobile/classschedule.html')
	c = Context({'course':course_list})
	print course_list
	return HttpResponse(t.render(c))

def exam_timetable(request, id, limit=100):
	#course_list = Course.objects.filter(department__id=id)
	#ids = [course.id for course in course_list]
	#exam_list = Exam.objects.filter(course__id__in=ids)
	# --or--
	# exam_list = Exam.objects.filter(course__department__id=id) # (not sure if this works with django-nonrel)
        department_list = Department.objects.get(pk=id)
	exam_list = Exam.objects.filter(department__id=id)

	'''
	department = Department.objects.get(pk=id)
	exam_list = Exam.objects.filter(course in list of courses
	course_list = Course.objects.all(post_pk = id)
	timetable_list= TimeTable.objects.all()
	'''
	t = loader.get_template('mobile/exam.html')
	c = Context({'department':department_list, 'exams':exam_list})
	return HttpResponse(t.render(c))

def home(request):
	t = loader.get_template('mobile/home.html')
	c = Context(dict())
	return HttpResponse(t.render(c))

def faculty_options(request, id):
	t = loader.get_template('mobile/departmentlist.html')
	c = Context({'id':id})
	return HttpResponse(t.render(c))
	

#Ansah's Views
def emergency_list(request):
    emergency_list = Emergency.objects.all()
    t = loader.get_template('mobile/emergencylist.html')
    c = Context({'emergency_list':emergency_list})
    return HttpResponse(t.render(c))

@csrf_exempt
def emergency_detail(request, id):
    emergency = Emergency.objects.get(pk=id)
    t = loader.get_template('mobile/emergencydetail.html')
    c = Context({'emergency':emergency})
    return HttpResponse(t.render(c))

def picture_list(request):
    picture_list = Picture.objects.all()
    t = loader.get_template('mobile/picturelist.html')
    c = Context({'picture_list':picture_list})
    return HttpResponse(t.render(c))

@csrf_exempt
def picture_detail(request, id):
    picture = Picture.objects.get(pk=id)
    t = loader.get_template('mobile/picturedetail.html')
    c = Context({'picture':picture})
    return HttpResponse(t.render(c))

def calendar_list(request):
	calendar_list = Calendar.objects.all()
	t = loader.get_template('mobile/calendarlist.html')
	c = Context({'calendar_list':calendar_list})
	return HttpResponse(t.render(c))

def calendar_detail(request,semester):
	events = Calendar.objects.filter(semester = semester)
	return render_to_response('mobile/calendardetail.html',{'events':events})

