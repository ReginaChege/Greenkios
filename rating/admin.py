from django.contrib import admin

# Register your models here.
from .models import Rate
class RegistrationAdmin(admin.ModelAdmin):
    list_display=("review_message","date")
admin.site.register(Rate,RegistrationAdmin)