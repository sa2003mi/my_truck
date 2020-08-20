from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Old_Parts
from service.models import Service
from django.urls import reverse_lazy
from .forms import Old_PartsForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.translation import ugettext, activate, get_language


# Create your views here.


class Old_PartsList(ListView):
    model = Old_Parts
    context_object_name = 'old_parts'
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


class Old_PartsDetail(DetailView):
    model = Old_Parts


class Old_PartsCreate(CreateView):
    model = Old_Parts
    template_name = 'old_parts/old_parts_add.html'
    form_class = Old_PartsForm
    queryset = Old_Parts.objects.all()
    success_url = '/old_parts'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class Old_PartsUpdate(UpdateView):
    model = Old_Parts
    template_name = 'old_parts/old_parts_add.html'
    form_class = Old_PartsForm
    success_url = '/old_parts'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Old_Parts, pk=pk_)

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class Old_PartsDelete(DeleteView):
    model = Old_Parts
    template_name = 'old_parts/old_parts_delete.html'
    success_url = '/old_parts'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Old_Parts, pk=pk_)
