from django.contrib import admin

# Register your models here.
from .models import Deliver
class DeliveryAdmin(admin.ModelAdmin):
     list_display = ("date", "delivery_cost", "order_status", "delivery_method", "delivery_person")

admin.site.register(Deliver, DeliveryAdmin)