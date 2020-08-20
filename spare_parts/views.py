from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Spare_Parts
from service.models import Service
from django.urls import reverse_lazy
from .forms import Spare_PartsForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.translation import ugettext, activate, get_language


# Create your views here.


class Spare_PartsList(ListView):
    model = Spare_Parts
    context_object_name = 'spare_parts'
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


class Spare_PartsDetail(DetailView):
    model = Spare_Parts


class Spare_PartsCreate(CreateView):
    model = Spare_Parts
    template_name = 'spare_parts/spare_parts_add.html'
    form_class = Spare_PartsForm
    queryset = Spare_Parts.objects.all()
    success_url = '/spare_parts'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class Spare_PartsUpdate(UpdateView):
    model = Spare_Parts
    template_name = 'spare_parts/spare_parts_add.html'
    form_class = Spare_PartsForm
    success_url = '/spare_parts'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Spare_Parts, pk=pk_)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class Spare_PartsDelete(DeleteView):
    model = Spare_Parts
    template_name = 'spare_parts/spare_parts_delete.html'
    success_url = '/spare_parts'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Spare_Parts, pk=pk_)
