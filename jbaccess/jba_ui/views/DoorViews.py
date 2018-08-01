from django.urls import reverse

from jba_core.models import Door
from jba_core.service import DoorService
from jba_ui.common.CommonViews import ListView, DetailView, CreateView, UpdateView, DeleteView
from jba_ui.common.model_types import DOOR
from jba_ui.common.view_fields import ID
from jba_ui.forms import DoorForm


class DoorListView(ListView):
    template_name = 'doors/doors-list.html'
    title = 'Doors list'
    model = Door
    model_name = DOOR
    fields = ['id', 'name', 'access_id']

    def get_queryset(self):
        return DoorService.get_all()


class DoorDetailsView(DetailView):
    template_name = 'doors/door-details.html'
    fields = ['id', 'name', 'access_id']
    title = 'Door details'

    def get_object(self, queryset=None):
        return DoorService.get(id=self.kwargs[ID])


class DoorCreateView(CreateView):
    template_name = 'doors/door-create.html'
    title = 'Create door'
    form_class = DoorForm

    def get_success_url(self):
        return reverse('ui:controller list')


class DoorUpdateView(UpdateView):
    template_name = 'doors/door-update.html'
    form_class = DoorForm
    title = 'Update door'

    def get_object(self, queryset=None):
        return DoorService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:controller details', kwargs={ID: self.kwargs[ID]})


class DoorDeleteView(DeleteView):
    template_name = 'doors/door-delete.html'
    title = 'Delete door'

    def get_object(self, queryset=None):
        return DoorService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:controller list')