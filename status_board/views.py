from django.shortcuts import render, redirect
from status_board.models import bridgeTable, Escalators, Elevators, message, domIntPBS, domIntBaggageSystems
from .forms import bridgeTableForm, elevatorForm, escalatorForm, messageForm, domIntPBSForm, domIntBaggageForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def home(request):
	# Display all systems ie user is authenticated
	# if request.user.is_authenticated:
		bridgeTableData = bridgeTable.objects.order_by('bridgeTableID')
		elevatorData = Elevators.objects.order_by('elevatorID')
		#escalatorData = Escalators.object.order_by('escalatorID')
		domIntPBSData = domIntPBS.objects.order_by('domIntPBSID')
		domIntBaggageData = domIntBaggageSystems.objects.order_by('domIntBaggageID')
		context = {
			'bridges': bridgeTableData,
			'elevators': elevatorData,
			'domIntPBS': domIntPBSData,
			'domIntBaggage': domIntBaggageData,
			#'escalators': escalatorData,
		}
		return render(request, 'status_board/home.html', context)


	# Display only bridgeTable, elevaotrData, escalatorData ie view for airline employees
	# else:
	# 	bridgeTableData = bridgeTable.objects.order_by('bridgeTableID')
# 		elevatorData = Elevators.objects.order_by('elevatorID')
# 		escalatorData = Escalators.object.order_by('escalatorID')
	#
	#
	# 	context = {
	# 		'bridges': bridgeTableData,
	# 		'elevators': elevatorData,
	#		'escalators': escalatorData,
	# 	}
	# 	return render(request, 'status_board/home.html', context)



#Update the bridge table
def bridgeTableUpdate(request, btID):
	btID = int(btID)
	tableID = bridgeTable.objects.filter(bridgeTableID=btID).first()
	form = bridgeTableForm(request.POST or None, instance=tableID)
	path = 'fromBridgeTable'

	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

#Update the elevator table
def elevatorUpdate(request, btID):
	#btID = int(btID)
	tableID = Elevators.objects.filter(elevatorID=btID).first()
	form = elevatorForm(request.POST or None, instance=tableID)
	path = 'fromElevator'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

#Update the escalotor table
def escalatorUpdate(request, btID):
	btID = int(btID)
	tableID = Escalators.objects.filter(escalatorID=btID).first()
	form = escalatorForm(request.POST or None, instance=tableID)
	path = 'fromEscalator'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

# Update pre board screening tables
# Update domIntPBS Table
def domIntPBSUpdate(request, btID): 
	btID = int(btID)
	tableID = domIntPBS.objects.filter(domIntPBSID=btID).first()
	form = domIntPBSForm(request.POST or None, instance=tableID)
	path = 'fromDomIntPBS'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

# Update tbPBS Table
def domIntPBSUpdate(request, btID): 
	btID = int(btID)
	tableID = tbPBS.objects.filter(tbPBSID=btID).first()
	form = tbPBSForm(request.POST or None, instance=tableID)
	path = 'fromTbPBS'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

# Update baggage tables 
def domIntBaggageUpdate(request, btID): 
	btID = int(btID)
	tableID = domIntBaggageSystems.objects.filter(domIntBaggageID=btID).first()
	form = domIntBaggageForm(request.POST or None, instance=tableID)
	path = 'fromDomIntBaggage'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

#Update the message table
def messageUpdate(request):

	tableID = message.objects.first()
	form = messageForm(request.POST or None, instance=tableID)
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
	}
	return render(request, 'status_board/forms.html', context)

