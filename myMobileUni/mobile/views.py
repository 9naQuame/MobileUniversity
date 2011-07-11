from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import New, Event, Announcement
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt

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
	class Meta:
		model = Event
		exclude = ['eventtype','approval']

def add_event(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		return HttpResponseRedirect('mobile/eventlist')
	else:
		form = EventForm()
	t = loader.get_template('mobile/eventadd.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))

