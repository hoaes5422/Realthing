from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("hello world!")

def greet(request, name):
	return HttpResponse(f"hello, {name}")

