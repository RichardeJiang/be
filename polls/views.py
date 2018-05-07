# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

import json

from utils import parseCSVFileFromDjangoFile, parseCSVFile, isNumber

# Create your views here.
# Note: a view is a func taking the HTTP request and returns sth accordingly

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
	return HttpResponse("<h1>This is the very first HTTP request!</h1>")

# Note: csr: cross site request, adding this to enable request from localhost
@csrf_exempt
def uploadCSV(request):
	print "Inside the upload function"
	if request.FILES:
		print "There is file!"
		csvFile = request.FILES['file']
		print request.FILES
		print type(csvFile)
		secondRowContent = parseCSVFile(csvFile)
		if request.POST:
	# if request.POST and request.FILES:
	# current problem: request from axios not recognized as POST
			csvFile = request.FILES['file']
			print "Now we got the csv file"

		return HttpResponse(json.dumps(secondRowContent))
		# return HttpResponse("Got the CSV file.")
	else:
		print "Not found the file!"
		return HttpResponseNotFound('Page not found for CSV')