from django import forms
from .models import Spare_Parts


class Spare_PartsForm(forms.ModelForm):

    class Meta:
        model = Spare_Parts
        exclude=['user','created_by']
    