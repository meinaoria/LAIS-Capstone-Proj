from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='status-board-home'),
    path('legend/',views.legend,name='legend'),
    path('updateSys/',views.updateSys, name='updateSys'),
    path('update/<id>/<sys>/<oldStat>/',views.update, name='update'),
]
