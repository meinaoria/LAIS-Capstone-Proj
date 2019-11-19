from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Escalators)
admin.site.register(Elevators)
admin.site.register(bridgeTable)
admin.site.register(message)
admin.site.register(domIntPBS)
admin.site.register(tbPBS)
admin.site.register(domIntBaggageSystems)
admin.site.register(tbBaggageSystems)
admin.site.register(tbOversize)
admin.site.register(domIntOversize)
admin.site.register(lavHut)
admin.site.register(electricalCharging)
admin.site.register(waterFill)

