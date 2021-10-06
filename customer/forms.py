from django import forms
from django.db.models import fields
from .models import Customer



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','email')

    
    
    