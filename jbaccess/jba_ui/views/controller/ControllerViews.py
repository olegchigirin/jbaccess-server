from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from jba_core.models import Controller
from jba_core.service import ControllerService
from jba_ui.common.mixins import DetailsUrlMixin, TitleMixin, ModelFieldsMixin, IdToContextMixin
from jba_ui.common.view_fields import ID
from jba_ui.forms import ControllerForm


class ControllerList(ListView, TitleMixin, ModelFieldsMixin, DetailsUrlMixin):
    template_name = 'controllers/controller-list.html'
    title = 'Controller list'
    model = Controller
    details_url_name = 'ui:controller details'
    fields = ['id', 'name', 'controller_id']

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
