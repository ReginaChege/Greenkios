from django.contrib import admin

# Register your models here.
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display=("amount","order","date","method_payment")
admin.site.register(Payment,PaymentAdmin)