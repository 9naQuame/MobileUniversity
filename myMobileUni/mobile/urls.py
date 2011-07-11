from django.conf.urls.defaults import *
urlpatterns = patterns('',
    #url(r'^$', 'mobile.views.home'),
    url(r'^newslist/(\d+)?$', 'mobile.views.news_list'),
    url(r'^newsdetail/(?P<id>\d+)/(\d+)?$', 'mobile.views.news_detail'),
    url(r'^eventlist/(\d+)?$', 'mobile.views.event_list'),
    url(r'^eventdetail/(?P<id>\d+)/(\d+)?$', 'mobile.views.event_detail'),
    url(r'^announcementlist/(\d+)?$', 'mobile.views.announcement_list'),
    url(r'^emergencylist/$', 'mobile.views.emergency_list'),
    url(r'^emergencydetail/(?P<id>\d+)/$','mobile.views.emergency_detail'),
    url(r'^emergencysearch/(\w*)$','mobile.views.emergency_search'),
    url(r'^picturelist/$', 'mobile.views.picture_list'),
    url(r'^picturedetail/(?P<id>\d+)/$','mobile.views.picture_detail'),
    url(r'^academiccalendar/$','mobile.views.calendar'),
)

