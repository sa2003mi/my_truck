from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Auto_Roof
from service.models import Service
from django.urls import reverse_lazy
from .forms import Auto_RoofForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.translation import ugettext, activate, get_language

# Create your views here.


class Auto_RoofList(ListView):
    model = Auto_Roof
    context_object_name = 'auto_roof'
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


class Auto_RoofDetail(DetailView):
    model = Auto_Roof


class Auto_RoofCreate(CreateView):
    model = Auto_Roof
    template_name = 'auto_roof/auto_roof_add.html'
    form_class = Auto_RoofForm
    queryset = Auto_Roof.objects.all()
    success_url = '/auto_roof'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class Auto_RoofUpdate(UpdateView):
    model = Auto_Roof
    template_name = 'auto_roof/auto_roof_add.html'
    form_class = Auto_RoofForm
    success_url = '/auto_roof'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Auto_Roof, pk=pk_)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class Auto_RoofDelete(DeleteView):
    model = Auto_Roof
    template_name = 'auto_roof/auto_roof_delete.html'
    success_url = '/auto_roof'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Auto_Roof, pk=pk_)
