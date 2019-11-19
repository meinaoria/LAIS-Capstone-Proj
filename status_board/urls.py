from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import UpdateForm


urlpatterns = [
    path('', views.home, name='status-board-home'),
    path('updateSys/',views.updateSys, name='updateSys'),
    path('update/<id>/<sys>/',views.update, name='update'),
    path('updateForm/<pk>/',UpdateForm.as_view(),name='updateForm'),
    path('bsForm/', views.bsForm, name = 'bsForm'),
    path('update/bridge/<btID>/', views.bridgeTableUpdate, name='bridgeTableForm'),
    path('update/elevator/<elevBtID>/', views.elevatorUpdate, name='elevatorForm'),
    path('update/escalator/<btID>/', views.escalatorUpdate, name='escalatorForm'),
    path('update/message/<btID>/', views.messageUpdate, name='messageForm'),
    path('update/domIntPBS/<btID>/', views.domIntPBSUpdate, name='domIntPBSForm'),
    path('update/tbPBS/<btID>/', views.tbPBSUpdate, name='tbPBSForm'),
    path('update/domIntBaggage/<btID>/', views.domIntBaggageUpdate, name='domIntBaggageForm'),


    path('update/tbBaggageSystems/<btID>/', views.tbBaggageSystemsUpdate, name='tbBaggageSystemsForm'),
    path('update/tbOversize/<btID>/', views.tbOversizeUpdate, name='tbOversizeForm'),
    path('update/domIntOversize/<btID>/', views.domIntOversizeUpdate, name='domIntOversizeForm'),
    path('update/lavHut/<btID>/', views.lavHutUpdate, name='lavHutForm'),
    path('update/electricalCharging/<btID>/', views.electricalChargingUpdate, name='electricalChargingForm'),
    path('update/waterFill/<btID>/', views.waterFillUpdate, name='waterFillForm'),
  
]
