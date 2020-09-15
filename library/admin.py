from django.contrib import admin
from .models import IC_SENSOR,IC_RF,MECHANICAL,INTERFACE_LOGIC,IC_MEMORY,IC_CLASS_A,ANALOG_POWER,PASSIVE,CLOCK_TIMING,CONNECTOR,DISCRETE_ANALOG,ELECTRO_MECHANICAL
# Register your models here.

admin.site.register(PASSIVE)
admin.site.register(CLOCK_TIMING)
admin.site.register(CONNECTOR)
admin.site.register(DISCRETE_ANALOG)
admin.site.register(ELECTRO_MECHANICAL)
admin.site.register(ANALOG_POWER)
admin.site.register(IC_CLASS_A)
admin.site.register(IC_MEMORY)
admin.site.register(INTERFACE_LOGIC)
admin.site.register(MECHANICAL)
admin.site.register(IC_RF)
admin.site.register(IC_SENSOR)