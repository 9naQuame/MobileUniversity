from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import new, event, announcement
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

