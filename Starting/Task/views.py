from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class Newtask(forms.Form):
	task = forms.CharField(label="New task")
	# priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def list(request):
	if "tasks" not in request.session:
		request.session["tasks"] = []
	return render(request,"list.html",{

		"tasks": request.session["tasks"]
		})

def add(request):
	if request.method == "POST":
		form = Newtask(request.POST)
		if form.is_valid():
			task = form.cleaned_data["task"]
			if task == "Delete":
				request.session["tasks"] = []
				return HttpResponseRedirect(reverse("tasks:list"))
			else:
				request.session["tasks"] += [task]
				return HttpResponseRedirect(reverse("tasks:list"))
		else:
			return render(request, "add.html",{
				"form": form 
				})
	return render(request,"add.html",{
		"form":  Newtask()

		})
