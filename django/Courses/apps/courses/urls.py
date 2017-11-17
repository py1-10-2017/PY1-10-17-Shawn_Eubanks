from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/(?P<course_id>\d+)/destroy_request$', views.destroy_request),
    url(r'^courses/(?P<course_id>\d+)/destroy$', views.destroy),
    url(r'^courses/create$', views.create),
]