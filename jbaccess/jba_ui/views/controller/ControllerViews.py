from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView

from jba_core.models import Controller
from jba_core.service import ControllerService
from jba_ui.common.mixins import TitleMixin, ModelFieldsMixin, IdToContextMixin
from jba_ui.common.view_fields import ID
from jba_ui.forms import ControllerForm
from jba_ui.tables import ControllerTable


class ControllerList(SingleTableView, TitleMixin):
    template_name = 'controllers/list.html'
    title = 'Controller list'
    model = Controller
    table_class = ControllerTable

    def get_queryset(self):
        return ControllerService.get_all()


class ControllerDetails(DetailView, TitleMixin, ModelFieldsMixin):
    template_name = 'controllers/controller-details.html'
    fields = ['id', 'name', 'controller_id']
    title = 'Controller details'

    def get_object(self, queryset=None):
        return ControllerService.get(id=self.kwargs[ID])


class ControllerCreate(CreateView, TitleMixin):
    template_name = 'controllers/controller-create.html'
    title = 'Create controller'
    form_class = ControllerForm

    def get_success_url(self):
        return reverse('ui:controller list')


class ControllerUpdate(UpdateView, TitleMixin, IdToContextMixin):
    template_name = 'controllers/controller-update.html'
    form_class = ControllerForm
    title = 'Update controller'

    def get_object(self, queryset=None):
        return ControllerService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:controller details', kwargs={ID: self.kwargs[ID]})


class ControllerDelete(DeleteView, TitleMixin, IdToContextMixin):
    template_name = 'controllers/controller-delete.html'
    title = 'Delete controller'

    def get_object(self, queryset=None):
        return ControllerService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:controller list')
