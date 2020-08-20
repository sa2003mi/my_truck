from django import forms
from .models import Auto_Roof


class Auto_RoofForm(forms.ModelForm):

    class Meta:
        model = Auto_Roof
        exclude = ['user', 'created_by']
