from django.contrib import admin

# Register your models here.
from .models import Elevator, Escalator

admin.site.register(Elevator)
admin.site.register(Escalator)