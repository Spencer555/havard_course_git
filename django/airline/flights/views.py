from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponseRedirect
# Create your views here.

from .models import Flight, Airport, Passanger



def index(request):
    return render(request, "flights/index.html", {
        "flights":Flight.objects.all()
    })
    
    
def flight(request, pk):
    flight = Flight.objects.get(pk=pk)
    return render(request, "flights/detail.html", {"flight":flight, "passengers":flight.passengers.all(), "non_passengers":Passanger.objects.exclude(flight=flight).all()})


def book(request, id):
    
    if request.method == "POST":
        flight = Flight.objects.get(id=id)
        passenger = Passanger.objects.get(id=int(request.POST["passenger"]) )
        passenger.flight.add(flight)
        
    return HttpResponseRedirect(reverse('flights:detail', args=(flight.id,)))
    