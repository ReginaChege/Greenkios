from django.contrib import admin

# Register your models here.
from .models import Basket
class BasketAdmin(admin.ModelAdmin):
 list_display=('basket_name','basket_number','items_baskets','created_at','updated_at')
admin.site.register(Basket,BasketAdmin)