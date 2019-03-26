from django.contrib import admin
from .models import Elevators,Escalators,bridgeTable, message
# Register your models here.

admin.site.register(Escalators)
admin.site.register(Elevators)
admin.site.register(bridgeTable)
admin.site.register(message)