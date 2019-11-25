from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Escalators)
admin.site.register(Elevators)
admin.site.register(bridgeTable)
admin.site.register(message)
admin.site.register(bagCarousel)
admin.site.register(domIntBaggageSystems)
admin.site.register(tbBaggageSystems)
admin.site.register(tbOversize)
admin.site.register(domIntOversize)


