from django.shortcuts import render, redirect
from status_board.models import *
# bridgeTable, Escalators, Elevators, message, domIntPBS,domIntBaggageSystems, tbPBS, tbBaggageSystems, tbOversize

from .forms import *
# bridgeTableForm, elevatorForm, escalatorForm, messageForm, domIntPBSForm, domIntBaggageSystemsForm, tbPBSForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def home(request):
	# Display all systems ie user is authenticated
	# if request.user.is_authenticated:
		bridgeTableData = bridgeTable.objects.order_by('bridgeTableID')
		elevatorData = Elevators.objects.order_by('elevatorID')
		escalatorData = Escalators.objects.order_by('escalatorID')
		domIntPBSData = domIntPBS.objects.order_by('domIntPBSID')
		domIntBaggageData = domIntBaggageSystems.objects.order_by('domIntBaggageID')

		context = {
			'bridges': bridgeTableData,
			'elevators': elevatorData,
			'escalators': escalatorData,
			'domIntPBS': domIntPBSData,
			'domIntBaggage': domIntBaggageData,
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

#Update the elevator table
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

#Update the escalator table
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
def tbPBSUpdate(request, btID):
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

# Update baggage table
def domIntBaggageUpdate(request, btID):
	btID = int(btID)
	tableID = domIntBaggageSystems.objects.filter(domIntBaggageID=btID).first()
	form = domIntBaggageSystemsForm(request.POST or None, instance=tableID)
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

# Update tb baggage table
def tbBaggageSystemsUpdate(request, btID):
	btID = int(btID)
	tableID = tbBaggageSystems.objects.filter(domIntBaggageID=btID).first()
	form = tbBaggageSystemsForm(request.POST or None, instance=tableID)
	path = 'fromTbBaggage'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

# Update tb oversize table
def tbOversizeUpdate(request, btID):
	btID = int(btID)
	tableID = tbOversize.objects.filter(domIntBaggageID=btID).first()
	form = tbOversizeForm(request.POST or None, instance=tableID)
	path = 'fromTbOversize'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

# Update domInt oversize table
def domIntOversizeUpdate(request, btID):
	btID = int(btID)
	tableID = domIntOversize.objects.filter(domIntBaggageID=btID).first()
	form = domIntOversizeForm(request.POST or None, instance=tableID)
	path = 'fromDomIntOversize'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

# Update lav hut table
def lavHutUpdate(request, btID):
	btID = int(btID)
	tableID = lavHut.objects.filter(domIntBaggageID=btID).first()
	form = lavHutForm(request.POST or None, instance=tableID)
	path = 'fromLavHut'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

# Update electrical Charging table
def electricalChargingUpdate(request, btID):
	btID = int(btID)
	tableID = electricalCharging.objects.filter(domIntBaggageID=btID).first()
	form = electricalChargingForm(request.POST or None, instance=tableID)
	path = 'fromElectricalCharging'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

# Update water Fill table
def waterFillUpdate(request, btID):
	btID = int(btID)
	tableID = waterFill.objects.filter(domIntBaggageID=btID).first()
	form = waterFillForm(request.POST or None, instance=tableID)
	path = 'fromWaterFill'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)




