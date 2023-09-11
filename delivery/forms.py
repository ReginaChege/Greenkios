from django import forms
from .models import Deliver

class DeliveryForm(forms.ModelForm):
    class Meta:
        model=Deliver
        fields="__all__"