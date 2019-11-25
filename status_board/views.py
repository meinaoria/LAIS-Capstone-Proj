from django.shortcuts import render, redirect
from status_board.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import IntegerField
from django.db.models.functions import Cast, Substr
from django.views.generic.edit import UpdateView
# bridgeTable, Escalators, Elevators, message, domIntPBS,domIntBaggageSystems, tbPBS, tbBaggageSystems, tbOversize
from datetime import datetime
from .forms import *
# bridgeTableForm, elevatorForm, escalatorForm, messageForm, domIntPBSForm, domIntBaggageSystemsForm, tbPBSForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
# Create your views here.

from django.db.models.expressions import F, Value, Func 


def legend(request):
	return render(request, 'status_board/legend.html')

#@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
def updateSys(request):
	if request.method == 'POST':
		sys = request.POST.get('system')
		id = request.POST.get('ID') 
		if sys == 'Elevator':
			context = updateElev(sys,id)
		elif sys == 'Escalator':
			context = updateEsc(sys,id)
		elif sys == 'bridge':
			context = updateBridge(sys,id)
		elif sys == 'PCA':
			context = updatePCA(sys,id)
		elif sys == 'GPU':
			context = updateGPU(sys,id)
		elif sys == 'Carousel':
			context = updateCarousel(sys,id)
		elif sys == 'mes':
			context = updateMes(sys,id)
	return render(request, 'status_board/ModalForms.html', context)

def updateCarousel(sys,id):
	carousel = bagCarousel.objects.filter(bagCarouselID=id).first()
	form = bagCarouselForm(instance=carousel)
	downTime = carousel.updated
	diff = datetime.now()- downTime
	dif = format_timedelta(diff)
	Status = carousel.bagCarousel_Status_Choice
	context= {
		'system':sys,
		'id':id,
		'downTime':dif,
		'form':form,
		'status':Status,
	}
	return context
	return

def updateEsc(sys,id):
	escalator = Escalators.objects.filter(escalatorID=id).first()
	form = escalatorForm(instance=escalator)
	downTime = escalator.updated
	diff = datetime.now()- downTime
	dif = format_timedelta(diff)
	Status = escalator.Escalator_Status_Choice
	context= {
		'system':sys,
		'id':id,
		'downTime':dif,
		'form':form,
		'status':Status,
	}
	return context

def updateMes(sys,id):
	mes = message.objects.filter(messageID=id).first()
	form =  messageForm(instance=mes)
	context={
		'system':sys,
		'id':id,
		'form':form,
	}
	return context

def updateElev(sys,id):
	elevator = Elevators.objects.filter(elevatorID=id).first()
			#get_object_or_404(Elevators, elevatorID=id)
	# print(elevator.Elevator_Status_Choice)
	form = elevatorForm(instance=elevator)
	downTime = elevator.updated
	diff = datetime.now() - downTime
	dif = format_timedelta(diff)
	# print((diff))
	# print('the diff time is')
	Status = elevator.Elevator_Status_Choice
	context= {
		'system':sys,
		'id':id,
		'downTime':dif,
		'form':form,
		'status':Status,
	}
	return context

#Bring up Bridge form
def updateBridge(sys,id):
	print('updateBridge')
	bridge = bridgeTable.objects.filter(bridgeTableID=id).first()
	form = bridgeTableForm(instance=bridge)
	downTime = bridge.bridgeUpdated
	diff = datetime.now()- downTime
	dif = format_timedelta(diff)
	Status = bridge.Bridge_Status_Choice
	context = {
		'system':sys,
				'id':id,
				'downTime':dif,
				'form':form,
				'status': Status,
	}
	return context

# Bring up PCA form
def updatePCA(sys,id):
	pca = bridgeTable.objects.filter(bridgeTableID=id).first()
	form = pcaTableForm(instance=pca)
	downTime = pca.pcaUpdated
	diff = datetime.now()- downTime
	dif = format_timedelta(diff)
	Status = pca.PCA_Status_Choice
	context = {
		'system':sys,
				'id':id,
				'downTime':dif,
				'form':form,
				'status': Status,
	}
	return context

# Bring up GPU form
def updateGPU(sys,id):
	gpu = bridgeTable.objects.filter(bridgeTableID=id).first()
	form = gpuTableForm(instance=gpu)
	downTime = gpu.gpuUpdated
	diff = datetime.now()- downTime
	dif = format_timedelta(diff)
	Status = gpu.GPU_Status_Choice
	context = {
		'system':sys,
				'id':id,
				'downTime':dif,
				'form':form,
				'status': Status,
	}
	return context

def format_timedelta(td):
    minutes, seconds = divmod(td.seconds + td.days * 86400, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

def update(request,id,sys,oldStat):
	context ={
			'sys':sys,
			'id':id,
		}
	if request.method == 'POST':		
		if sys == 'Elevator':
				elevator=get_object_or_404(Elevators, elevatorID=id)
				form = elevatorForm(request.POST, instance=elevator)
				status = 'Elevator_Status_Choice'
		elif sys == 'Escalator':
				escalator=get_object_or_404(Escalators, escalatorID=id)
				form = escalatorForm(request.POST, instance=escalator)
				status = 'Escalator_Status_Choice'
		elif sys == 'bridge':
				bridge=get_object_or_404(bridgeTable, bridgeTableID=id)
				form = bridgeTableForm(request.POST, instance = bridge)
				status = 'Bridge_Status_Choice'
		elif sys =='PCA':
				pca=get_object_or_404(bridgeTable, bridgeTableID=id)
				form = pcaTableForm(request.POST, instance = pca)
				status = 'PCA_Status_Choice'
		elif sys == 'GPU':
				gpu=get_object_or_404(bridgeTable, bridgeTableID=id)
				form = gpuTableForm(request.POST, instance = gpu)
				status = 'GPU_Status_Choice'
		elif sys == 'mes':
				mes=get_object_or_404(message,messageID=id)
				form = messageForm(request.POST, instance=mes)
				status = 'message'
		elif sys == 'Carousel':
				carousel = get_object_or_404(bagCarousel,bagCarouselID=id)
				form = bagCarouselForm(request.POST, instance = carousel)
				status = 'bagCarousel_Status_Choice'
		if form.is_valid():
			newStat = form.cleaned_data[status]
			if (oldStat == newStat):
				return render(request, 'status_board/form_notSaved.html',context)
			form.save()
	return render(request, 'status_board/form_saved.html',context)


def home(request):
	# Display all systems ie user is authenticated
	# if request.user.is_authenticated:
		bridgeTableData = bridgeTable.objects.order_by('bridgeTableID')
		rows = {1,2,5,6,9,10,13,14,17,18,21,22,25,26,29,30}
		elevatorData = Elevators.objects.order_by('elevatorTableID')
		escalatorData = Escalators.objects.order_by('escalatorTableID')
		bagCarousels = bagCarousel.objects.order_by('bagCarouselID')
		domIntBaggageData = domIntBaggageSystems.objects.order_by('domIntBaggageID')
		tbBaggageSystemData = tbBaggageSystems.objects.order_by('tbBaggageID')
		domIntOversizeData = domIntOversize.objects.order_by('domIntOversizeID')
		tbOversizeData = tbOversize.objects.order_by('tbOversizeID')
		messageData = message.objects.order_by('messageID')
	
	

		context = {
			'bridges': bridgeTableData,
			'rows':rows,
			'elevators': elevatorData,
			'escalators': escalatorData,
			'bagCarousel': bagCarousels,
			'fixedMessages': messageData,
			'domIntBaggage': domIntBaggageData,
			'tbBaggage': tbBaggageSystemData,
			'domIntOversize': domIntOversizeData,
			'tbOversize': tbOversizeData,
		}
		return render(request, 'status_board/home.html', context)


	# Display only bridgeTable, elevaotrData, escalatorData ie view for airline employees
	# else:
	
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


@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
#Update the bridge table
def bridgeTableUpdate(request, btID):
	
	
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

@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
#Update the elevator table
def elevatorUpdate(request, elevBtID):
	
	tableID = Elevators.objects.filter(elevatorID=elevBtID).first()
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
	return render(request, 'status_board/forms.html',context)

@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
#Update the escalator table
def escalatorUpdate(request, btID):
	
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

@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
#Update the message table
def messageUpdate(request, btID ):
	tableID = message.objects.filter(messageID=btID).first()
	form = messageForm(request.POST or None, instance=tableID)
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
# Update pre board screening tables
# Update domIntPBS Table
def domIntPBSUpdate(request, btID):
	
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

@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
# Update tbPBS Table
def tbPBSUpdate(request, btID):
	
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

@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
# Update baggage table
def domIntBaggageUpdate(request, btID):
	
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


@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
# Update tb baggage table
def tbBaggageSystemsUpdate(request, btID):
	
	tableID = tbBaggageSystems.objects.filter(tbBaggageID=btID).first()
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

@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
# Update tb oversize table
def tbOversizeUpdate(request, btID):
	
	tableID = tbOversize.objects.filter(tbOversizeID=btID).first()
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

@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
# Update domInt oversize table
def domIntOversizeUpdate(request, btID):
	
	tableID = domIntOversize.objects.filter(domIntOversizeID=btID).first()
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


@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
# Update electrical Charging table
def electricalChargingUpdate(request, btID):
	
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

@user_passes_test(lambda u: u.has_perm('LAIS.has_write_access'))
# Update water Fill table
def waterFillUpdate(request, btID):
	
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

		

