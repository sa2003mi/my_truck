from django import forms
from .models import Old_Parts


class Old_PartsForm(forms.ModelForm):

    class Meta:
        model = Old_Parts
        exclude = ['user', 'created_by']
