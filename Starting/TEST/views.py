from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse



class Newname(forms.Form):
	name = forms.CharField(label="Your name")


def name(request):
	if "name2" not in request.session:
		request.session["name2"] = []
	return render(request,"name.html",{

		"names": request.session["name2"]
		})

def index(request):
	if request.method == "POST":
		formname = Newname(request.POST)
		if formname.is_valid():
			name1 = formname.cleaned_data["name"]
			if name1 == "Delete":
				request.session["name2"] = []
				return HttpResponseRedirect(reverse("names:name"))	
			else:
				request.session["name2"] += [name1]
				return HttpResponseRedirect(reverse("names:name"))		
		else:
			return render(request, "table.html",{
				"form": formname 
				})
	return render(request,"table.html",{
		"form":  Newname()

		})
	return render(request, "table.html")














