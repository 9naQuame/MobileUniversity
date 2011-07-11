from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import new, event, announcement, Faculty, Department,Course, Exam
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt

def news_list(request, limit=60):
	news_list = new.objects.all()
	t = loader.get_template('news/list.html')
	c = Context({'news_list':news_list})
	return HttpResponse(t.render(c))

def announcement_list(request, limit=120):
	announcement_list = announcement.objects.all()
	t = loader.get_template('announcement/list.html')
	c = Context({'announcement_list':announcement_list})
	return HttpResponse(t.render(c))

def event_list(request, limit=60):
	event_list = event.objects.all()
	t = loader.get_template('event/list.html')
	c = Context({'event_list':event_list})
	return HttpResponse(t.render(c))

def news_detail(request, id):
	news = new.objects.get(pk=id)
	t = loader.get_template('news/detail.html')
	c = Context({'news':news})
	return HttpResponse(t.render(c))

def event_detail(request, id):
	events = event.objects.get(pk=id)
	t = loader.get_template('event/detail.html')
	c = Context({'events':events})
	return HttpResponse(t.render(c))

class SearchForm(forms.Form):
	search = forms.CharField()

class EventForm(ModelForm):
	class Meta:
		model = event
		exclude = ['eventtype','approval']

def add_event(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		return HttpResponseRedirect('/event/list')

	else:
		form = EventForm()
	t = loader.get_template('event/add.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))

#Lady-Asaph
#faculty list
def faculty_list(request, limit=100):
	'''faculty_list = Faculty.objects.all()
	t = loader.get_template('mobile/facultylist.html')
	c = Context({'faculty':faculty_list})
	return HttpResponse(t.render(c))'''
	return HttpResponse('going to give a list')


def faculty_department(request, id, limit=100):
	faculty_list = Faculty.objects.get(pk=id)
	department_list = Department.objects.all(Faculty__id=id)
	t = loader.get_template('mobile/departmentlist.html')
	c = Context({'faculty':faculty_list, 'department':department_list})
	return HttpResponse(t.render(c))

def course_department(request, id, limit=100):
	department_list = Department.objects.get(pk=id)
	course_list = Course.objects.all(Department__id = id)
	t = loader.get_template('mobile/courselist.html')
	c = Context({'department':department_list, 'course':course_list})
	return HttpResponse(t.render(c))

def exam_timetable(request, id, limit=100):
	#course_list = Course.objects.filter(department__id=id)
	#ids = [course.id for course in course_list]
	#exam_list = Exam.objects.filter(course__id__in=ids)
	# --or--
	# exam_list = Exam.objects.filter(course__department__id=id) # (not sure if this works with django-nonrel)

	exam_list = Exam.objects.filter(department__id=id)
	#print exam_list

	'''
	department = Department.objects.get(pk=id)
	exam_list = Exam.objects.filter(course in list of courses
	course_list = Course.objects.all(post_pk = id)
	timetable_list= TimeTable.objects.all()
	'''
