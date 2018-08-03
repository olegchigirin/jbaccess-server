from django.urls import reverse

from jba_core.models import Place
from jba_core.service import PlaceService
from jba_ui.common.CommonViews import ListView, DetailView, CreateView, UpdateView, DeleteView
from jba_ui.common.view_fields import ID
from jba_ui.forms import PlaceForm


class PlaceListView(ListView):
    template_name = 'places/places-list.html'
    title = 'Place list'
    model = Place
    details_url_name = 'ui:place details'
    fields = ['id', 'name']

    def get_queryset(self):
        return PlaceService.get_all()


class PlaceDetailsView(DetailView):
    template_name = 'places/place-details.html'
    fields = ['id', 'name']
    title = 'Place details'

    def get_object(self, queryset=None):
        return PlaceService.get(id=self.kwargs[ID])


class PlaceCreateView(CreateView):
    template_name = 'places/place-create.html'
    title = 'Create place'
    form_class = PlaceForm

    def get_success_url(self):
        return reverse('ui:place list')


class PlaceUpdateView(UpdateView):
    template_name = 'places/place-update.html'
    form_class = PlaceForm
    title = 'Update place'

    def get_object(self, queryset=None):
        return PlaceService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:place details', kwargs={ID: self.kwargs[ID]})


class PlaceDeleteView(DeleteView):
    template_name = 'places/place-delete.html'
    title = 'Delete place'

    def get_object(self, queryset=None):
        return PlaceService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:place list')
