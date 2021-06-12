from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse



def index(request):
	return render(request,"flights.html",{
		"flights": Flight.objects.all(),
		})

def flight(request,flight_id):
	flight = Flight.objects.get(pk=flight_id)
	return render(request,"flightflight.html",{
		"flight": flight,
		"Passenger": flight.passenger.all(),
		"non_passenger": Passenger.objects.exclude(flights=flight).all()
		})

def book(request,flight_id):
	if request.method == "POST": 
		flight = Flight.objects.get(pk=flight_id)
		passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
		passenger.flights.add(flight)
		return HttpResponseRedirect(reverse('flight',args=(flight.id,)))