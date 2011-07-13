from django.conf.urls.defaults import *
urlpatterns = patterns('',
    url(r'^$', 'mobile.views.home'),
    url(r'^newslist/(\d+)?$', 'mobile.views.news_list'),
    url(r'^newsdetail/(?P<id>\d+)/(\d+)?$', 'mobile.views.news_detail'),
    url(r'^eventlist/(\d+)?$', 'mobile.views.event_list'),
    url(r'^eventadd/$', 'mobile.views.add_event'),
    url(r'^eventdetail/(?P<id>\d+)/(\d+)?$', 'mobile.views.event_detail'),
    url(r'^announcementlist/(\d+)?$', 'mobile.views.announcement_list'),
    url(r'^emergencylist/$', 'mobile.views.emergency_list'),
    url(r'^emergencydetail/(?P<id>\d+)/$','mobile.views.emergency_detail'),
    url(r'^emergencysearch/(\w*)$','mobile.views.emergency_search'),
    url(r'^picturelist/$', 'mobile.views.picture_list'),
    url(r'^picturedetail/(?P<id>\d+)/$','mobile.views.picture_detail'),
    url(r'^academiccalendar/$','mobile.views.calendar'),
    url(r'^faculty/$', 'mobile.views.faculty_list'),
    url(r'^departmentlist/(?P<id>\d+)/$', 'mobile.views.faculty_options'),
    url(r'^department/(?P<id>\d+)/$', 'mobile.views.faculty_department'),
    url(r'^course/(?P<id>\d+)','mobile.views.course_department'),
    url(r'^coursedetial/(?P<id>\d+)', 'mobile.views.coursedetial'),
    url(r'^classschedule/(?P<id>\d+)', 'mobile.views.classschedule'),
    url(r'^exam/(?P<id>\d+)', 'mobile.views.exam_timetable'),
)

