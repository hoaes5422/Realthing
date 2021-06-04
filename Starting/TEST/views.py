from django.shortcuts import render
from django.com import HttpResponse
def index(request):
	return	HttpResponse("Hello, world")
