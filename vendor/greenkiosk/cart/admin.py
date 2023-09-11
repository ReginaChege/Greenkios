from django.contrib import admin

# Register your models here.
from.models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display=("price","quantity","shippingcost","paymentoptions","image")
admin.site.register(Cart,CartAdmin)