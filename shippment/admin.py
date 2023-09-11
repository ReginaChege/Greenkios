from django.contrib import admin

# Register your models here.
from .models import Shipment
class ShipmentAdmin(admin.ModelAdmin):
    list_display=('name_origin','weight','destination','amount')
admin.site.register(Shipment,ShipmentAdmin)
