from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='status-board-home'),
]
