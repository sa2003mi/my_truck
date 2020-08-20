from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Service
from django.utils.translation import ugettext, activate, get_language


# Create your views here.



class ServiceList(ListView):
    model = Service
    

    

    

class ServiceDetail(DetailView):
    model = Service
    


