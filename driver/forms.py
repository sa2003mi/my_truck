from django import forms
from .models import Driver


class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        exclude=['user','created_by']
    