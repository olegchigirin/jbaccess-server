from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from jba_core.models import Door
from jba_ui.common.mixins import DetailsUrlMixin, TitleMixin, ModelFieldsMixin, IdToContextMixin
from jba_core.service import DoorService
from jba_ui.common.view_fields import ID
from jba_ui.forms import DoorForm


class DoorList(ListView, TitleMixin, DetailsUrlMixin, ModelFieldsMixin):
    template_name = 'doors/doors-list.html'
    title = 'Doors list'
    model = Door
    details_url_name = 'ui:door details'
    fields = ['id', 'name', 'access_id']

    def get_queryset(self):
        return DoorService.get_all()


class DoorDetails(DetailView, TitleMixin, ModelFieldsMixin, IdToContextMixin):
    template_name = 'doors/door-details.html'
    fields = ['id', 'name', 'access_id']
    title = 'Door details'

    def get_object(self, queryset=None):
        return DoorService.get(id=self.kwargs[ID])


class DoorCreate(CreateView, TitleMixin):
    template_name = 'doors/door-create.html'
    title = 'Create door'
    form_class = DoorForm

    def get_success_url(self):
        return reverse('ui:controller list')


class DoorUpdate(UpdateView, TitleMixin, IdToContextMixin):
    template_name = 'doors/door-update.html'
    form_class = DoorForm
    title = 'Update door'

    def get_object(self, queryset=None):
        return DoorService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:controller details', kwargs={ID: self.kwargs[ID]})


class DoorDelete(DeleteView, TitleMixin, IdToContextMixin):
    template_name = 'doors/door-delete.html'
    title = 'Delete door'

    def get_object(self, queryset=None):
        return DoorService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:door list')
