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
		elif sys == 'tbOversize':
			context = updateTbOversize(sys,id)
		elif sys == 'domIntOversize':
			context = updateDomIntOversize(sys,id)
		elif sys == 'tbBaggage':
			context = updateTbBaggage(sys,id)
		elif sys =='domIntBaggage':
			context = updateDomIntBaggage(sys,id)
			
	return render(request, 'status_board/ModalForms.html', context)

def updateDomIntBaggage(sys,id):
	domIntBag = domIntBaggageSystems.objects.filter(domIntBaggageID=id).first()
	form = domIntBaggageSystemsForm(instance=domIntBag)
	downTime = domIntBag.updated
	diff = datetime.now()- downTime
	dif = format_timedelta(diff)
	Status = domIntBag.DomIntBaggage_Status_Choice
	context= {
		'system':'Domestic and International Baggage',
		'id':id,
		'downTime':dif,
		'form':form,
		'status':Status,
	}
	return context

def updateTbBaggage(sys,id):
	tbBag = tbBaggageSystems.objects.filter(tbBaggageID=id).first()
	form = tbBaggageSystemsForm(instance=tbBag)
	downTime = tbBag.updated
	diff = datetime.now()- downTime
	dif = format_timedelta(diff)
	Status = tbBag.TbBaggage_Status_Choice
	context= {
		'system':'Transborder Baggage System',
		'id':id,
		'downTime':dif,
		'form':form,
		'status':Status,
	}
	return context

def updateDomIntOversize(sys,id):
	domIntOver = domIntOversize.objects.filter(domIntOversizeID=id).first()
	form = domIntOversizeForm(instance=domIntOver)
	downTime = domIntOver.updated
	diff = datetime.now()- downTime
	dif = format_timedelta(diff)
	Status = domIntOver.DomIntOversize_Status_Choice
	context= {
		'system':'Domestic and International Oversize',
		'id':id,
		'downTime':dif,
		'form':form,
		'status':Status,
	}
	return context


def updateTbOversize(sys,id):
	tbOver = tbOversize.objects.filter(tbOversizeID=id).first()
	form = tbOversizeForm(instance=tbOver)
	downTime = tbOver.updated
	diff = datetime.now()- downTime
	dif = format_timedelta(diff)
	Status = tbOver.TbOversize_Status_Choice
	context= {
		'system':'Transborder Oversize',
		'id':id,
		'downTime':dif,
		'form':form,
		'status':Status,
	}
	return context

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
	print('IN UPDATE MES ID is ' + id)
	mes = message.objects.filter(messageID=id).first()
	print(' Got MES')
	form =  messageForm(instance=mes)
	print('Got MES Form')
	Status = mes.message
	context={
		'system':sys,
		'id':id,
		'form':form,
		'status': Status
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
	
	if request.method == 'POST':	
		context ={
			'sys':sys,
			'id':id,
		}	
		print('SYS IS ' + sys)
		if sys == 'Elevator':
				system=get_object_or_404(Elevators, elevatorID=id)
				form = elevatorForm(request.POST, instance=system)
				status = 'Elevator_Status_Choice'
				fieldsToUpdate = 'all'
		elif sys == 'Escalator':
				system=get_object_or_404(Escalators, escalatorID=id)
				form = escalatorForm(request.POST, instance=system)
				status = 'Escalator_Status_Choice'
				fieldsToUpdate = 'all'
		elif sys == 'bridge':
				system = get_object_or_404(bridgeTable, bridgeTableID=id)
				form = bridgeTableForm(request.POST, instance = system)
				status = 'Bridge_Status_Choice'
				fieldsToUpdate = ['Bridge_Status_Choice','bridgeUpdated']
		elif sys =='PCA':
				system=get_object_or_404(bridgeTable, bridgeTableID=id)
				form = pcaTableForm(request.POST, instance = system)
				status = 'PCA_Status_Choice'
				fieldsToUpdate = ['PCA_Status_Choice','pcaUpdated']
		elif sys == 'GPU':
				system=get_object_or_404(bridgeTable, bridgeTableID=id)
				form = gpuTableForm(request.POST, instance = system)
				status = 'GPU_Status_Choice'
				fieldsToUpdate = ['GPU_Status_Choice','gpuUpdated']
		elif sys == 'mes':
				system =get_object_or_404(message,messageID=id)
				form = messageForm(request.POST, instance=system)
				status = 'message'
				fieldsToUpdate = 'all'
		elif sys == 'Carousel':
				system = get_object_or_404(bagCarousel,bagCarouselID=id)
				form = bagCarouselForm(request.POST, instance = system)
				status = 'bagCarousel_Status_Choice'
				fieldsToUpdate = 'all'
		elif sys == 'Transborder Oversize':
				system = get_object_or_404(tbOversize,tbOversizeID=id)
				form = tbOversizeForm(request.POST, instance = system)
				status = 'TbOversize_Status_Choice'
				fieldsToUpdate = 'all'
		elif sys == 'Domestic and International Oversize':
				system = get_object_or_404(domIntOversize,domIntOversizeID=id)
				form = domIntOversizeForm(request.POST, instance = system)
				status = 'DomIntOversize_Status_Choice'
				fieldsToUpdate = 'all'
		elif sys == 'Transborder Baggage System':
				system = get_object_or_404(tbBaggageSystems,tbBaggageID=id)
				form = tbBaggageSystemsForm(request.POST, instance = system)
				status = 'TbBaggage_Status_Choice'
				fieldsToUpdate = 'all'
		elif sys == 'Domestic and International Baggage':
				system = get_object_or_404(domIntBaggageSystems,domIntBaggageID=id)
				form = domIntBaggageSystemsForm(request.POST, instance = system)
				status = 'DomIntBaggage_Status_Choice'
				fieldsToUpdate = 'all'
		if form.is_valid():
				newStat = form.cleaned_data[status]
				if (oldStat == newStat):
					return render(request, 'status_board/form_notSaved.html',context)
				if (fieldsToUpdate == 'all'):
					form.save()
				else:
					system.save(update_fields=fieldsToUpdate)
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





		

