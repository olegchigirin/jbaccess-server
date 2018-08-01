from django.shortcuts import get_object_or_404
from django.urls import reverse

from jba_core.models import Controller
from jba_core.service import ControllerService
from jba_ui.common.CommonViews import ListView, DetailView, CreateView, UpdateView, DeleteView
from jba_ui.common.model_types import CONTROLLER
from jba_ui.common.view_fields import ID
from jba_ui.forms import ControllerForm


class ControllerListView(ListView):
    template_name = 'controllers/controller-list.html'
    title = 'Controller list'
    model = Controller
    model_name = CONTROLLER
    fields = ['id', 'name', 'controller_id']

    def get_queryset(self):
        return ControllerService.get_all()


class ControllerDetailsView(DetailView):
    template_name = 'controllers/controller-details.html'
    fields = ['id', 'name', 'controller_id']
    title = 'Controller details'

    def get_object(self, queryset=None):
        return ControllerService.get(id=self.kwargs[ID])


class ControllerCreateView(CreateView):
    template_name = 'controllers/controller-create.html'
    title = 'Create controller'
    form_class = ControllerForm

    def get_success_url(self):
        return reverse('ui:controller list')


class ControllerUpdateView(UpdateView):
    template_name = 'controllers/controller-update.html'
    form_class = ControllerForm
    title = 'Update controller'

    def get_object(self, queryset=None):
        return ControllerService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:controller details', kwargs={ID: self.kwargs[ID]})


class ControllerDeleteView(DeleteView):
    template_name = 'controllers/controller-delete.html'
    title = 'Delete controller'

    def get_object(self, queryset=None):
        return ControllerService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:controller list')
