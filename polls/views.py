# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.
# Note: a view is a func taking the HTTP request and returns sth accordingly

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
	return HttpResponse("<h1>This is the very first HTTP request!</h1>")

def uploadCSV(request):
	if request.POST and request.FILES:
		csvFile = request.FILES['file']

		return HttpResponse("<h1>Got the CSV file.</h1>")
	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')