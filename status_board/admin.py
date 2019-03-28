from django.contrib import admin
from .models import Elevators,Escalators,bridgeTable, message, domIntBaggageSystems
# Register your models here.

admin.site.register(Escalators)
admin.site.register(Elevators)
admin.site.register(bridgeTable)
admin.site.register(message)
admin.site.register(domIntBaggageSystems)