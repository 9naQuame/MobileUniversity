from django.conf.urls.defaults import *
urlpatterns = patterns('',
    #url(r'^$', 'mobile.views.home'),
    url(r'^newslist/(\d+)?$', 'mobile.views.news_list'),
    url(r'^newsdetail/(?P<id>\d+)/(\d+)?$', 'mobile.views.news_detail'),
    url(r'^eventlist/(\d+)?$', 'mobile.views.event_list'),
    url(r'^eventadd/$', 'mobile.views.add_event'),
    url(r'^eventdetail/(?P<id>\d+)/(\d+)?$', 'mobile.views.event_detail'),
    url(r'^announcementlist/(\d+)?$', 'mobile.views.announcement_list'),

)

