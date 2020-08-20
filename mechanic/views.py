from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mechanic 
from service.models import Service
from django.urls import reverse_lazy
from .forms import MechanicForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.translation import ugettext, activate, get_language


# Create your views here.


class MechanicList(ListView):
    model = Mechanic
    context_object_name = 'mechanic'
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

class MechanicDetail(DetailView):
    model = Mechanic



class MechanicCreate(CreateView):
    model = Mechanic 
    template_name = 'mechanic/mechanic_add.html'
    form_class = MechanicForm
    queryset = Mechanic.objects.all()
    success_url = '/mechanic'
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
   
    


class MechanicUpdate(UpdateView):
    model = Mechanic
    template_name = 'mechanic/mechanic_add.html'
    form_class = MechanicForm
    success_url = '/mechanic'
    
    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Mechanic , pk =pk_)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
   
    
    


class MechanicDelete(DeleteView):
    model = Mechanic
    template_name = 'mechanic/mechanic_delete.html'
    success_url = '/mechanic'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Mechanic, pk=pk_)
