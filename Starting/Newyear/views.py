from django.shortcuts import render
import datetime
def index(request):
	now = datetime.datetime.now()
	return render(request,"new.html",{
		"newyear": now.date  == 1 and now.month == 1

		}) 
