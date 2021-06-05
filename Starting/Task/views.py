from django.shortcuts import render


tasks = ["Check the homework",
"Write down the idea ",
"End the thing you start"]

def list(request):
	return render(request,"list.html",{

		"tasks": tasks
		})

def add(request):
	return render(request,"add.html")
