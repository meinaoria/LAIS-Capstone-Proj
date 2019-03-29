from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='status-board-home'),
    path('update/bridge/<btID>/', views.bridgeTableUpdate, name='bridgeTableForm'),
    path('update/elevator/<btID>/', views.elevatorUpdate, name='elevatorForm'),
    path('update/escalator/<btID>/', views.escalatorUpdate, name='escalatorForm'),
    path('update/message/', views.messageUpdate, name='messageForm'),
    path('update/domIntPBS/<btID>/', views.domIntPBSUpdate, name='domIntPBSForm'),
    path('update/domIntBaggage/<btID>/', views.domIntBaggageUpdate, name='domIntBaggageForm'),
]
