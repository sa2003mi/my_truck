from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Driver 
from service.models import Service
from django.urls import reverse_lazy
from .forms import DriverForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.translation import ugettext, activate, get_language

# Create your views here.


class DriverList(ListView):
    model = Driver
    context_object_name = 'driver'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(city__icontains=query)
                )
        else:
            object_list = self.model.objects.all()
        return object_list

class DriverDetail(DetailView):
    model = Driver



class DriverCreate(CreateView):
    model = Driver 
    template_name = 'driver/driver_add.html'
    form_class = DriverForm
    queryset = Driver.objects.all()
    success_url = '/driver'
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
   
    


class DriverUpdate(UpdateView):
    model = Driver
    template_name = 'driver/driver_add.html'
    form_class =DriverForm
    success_url = '/driver'
    
    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Driver , pk =pk_)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
   
    
    


class DriverDelete(DeleteView):
    model =Driver
    template_name = 'driver/driver_delete.html'
    success_url = '/driver'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Driver, pk=pk_)
