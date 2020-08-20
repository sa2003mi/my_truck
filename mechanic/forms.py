
from django import forms
from .models import Mechanic

class MechanicForm(forms.ModelForm):


    class Meta:
        model = Mechanic
        exclude=['user','created_by']
    
    

    
