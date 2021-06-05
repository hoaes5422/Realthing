from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return render(request, "table.html")

def greet(request, name):
	return render(request, "greet.html", {
		"name": name.capitalize()
		})




