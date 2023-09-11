from django.contrib import admin

# Register your models here.
from .models import MamaMboga
class VendorAdmin(admin.ModelAdmin):
    list_display=("name","storename","location","contact","password","username")
admin.site.register(MamaMboga,VendorAdmin)