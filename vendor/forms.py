from django import forms
from .models import MamaMboga
class VendorForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=MamaMboga
        fields="__all__"