# Project URLs
from django.conf.urls import patterns, include, url

urlpatterns = patterns('', url(r'^test/', 'polls.views.test', name = 'test'),)