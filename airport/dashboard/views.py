from django.shortcuts import render
from .models import Elevator, Escalator, BaggageBelt

# Create your views here.

# Return all elevators, escalators, etc... here
def dashboard(request):
	elevators = Elevator.objects.all()
	escalators = Escalator.objects.all()
	baggage_belts = BaggageBelt.objects.all()
	context = {
		'elevators': elevators,
		'escalators': escalators,
		'baggage_belts': baggage_belts,
	}
	return render(request, 'dashboard/dashboard.html', context)