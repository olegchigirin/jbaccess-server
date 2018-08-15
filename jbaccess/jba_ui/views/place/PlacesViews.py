
from django.http import HttpResponseRedirect
from django.urls import reverse

from jba_core.models import Place
from jba_core.service import PlaceService
from jba_ui.common.const import ID, NAME
from jba_ui.common.views import ModelListView, ModelCreateView, ModelDetailsView, ModelUpdateView, ModelDeleteView, \
    AttachedModelToModel, AttachModelToModel, DetachModelFromModel
from jba_ui.forms import PlaceCreateForm, DoorAttachForm, DoorDetachForm
from jba_ui.tables import PlaceTable, DoorTable


class PlaceList(ModelListView):
    template_name = 'places/list.html'
    title = 'Place list'
    model = Place
    table_class = PlaceTable
    service = PlaceService

    def get_queryset(self):
        return self.get_all()


class PlaceCreate(ModelCreateView):
    template_name = 'places/create.html'
    title = 'Create place'
    form_class = PlaceCreateForm
    place_id = None

    def form_valid(self, form: PlaceCreateForm):
        place = PlaceService.create(
            name=form.cleaned_data[NAME]
        )
        self.place_id = place.id
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:place list')


class PlaceDetails(ModelDetailsView):
    template_name = 'places/details.html'
    fields = ['id', 'name']
    title = 'Place details'
    service = PlaceService

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.kwargs[ID])


class PlaceUpdate(ModelUpdateView):
    template_name = 'places/update.html'
    form_class = PlaceCreateForm
    title = 'Update place'
    service = PlaceService

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.kwargs[ID])

    def form_valid(self, form: PlaceCreateForm):
        PlaceService.update(
            id=self.get_object().id,
            name=form.cleaned_data[NAME]
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:place details', kwargs={ID: self.get_object().id})


class PlaceDelete(ModelDeleteView):
    template_name = 'places/delete.html'
    title = 'Delete place'
    service = PlaceService

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.kwargs[ID])

    def delete(self, request, *args, **kwargs):
        PlaceService.delete(id=self.get_object().id)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:place list')


class PlaceAttachedDoors(AttachedModelToModel):
    template_name = 'places/attached-doors.html'
    table_class = DoorTable
    title = 'Attached doors'

    def get_queryset(self):
        return PlaceService.get_doors(id=self.kwargs[ID])


class PlaceAttachDoors(AttachModelToModel):
    template_name = 'places/attach-doors.html'
    title = 'Attach doors'
    form_class = DoorAttachForm

    def get_form_kwargs(self):
        kwargs = super(PlaceAttachDoors, self).get_form_kwargs()
        kwargs['place_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        place_id = self.kwargs[ID]
        doors = form.cleaned_data['doors']
        for door in doors:
            PlaceService.attach_door(place_id=place_id, door_id=door.id)
        return super(PlaceAttachDoors, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:place attached doors', kwargs={ID: self.kwargs[ID]})


class PlaceDetachDoors(DetachModelFromModel):
    template_name = 'places/detach-doors.html'
    title = 'Detach doors'
    form_class = DoorDetachForm

    def get_form_kwargs(self):
        kwargs = super(PlaceDetachDoors, self).get_form_kwargs()
        kwargs['place_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        place_id = self.kwargs[ID]
        doors = form.cleaned_data['doors']
        for door in doors:
            PlaceService.detach_door(place_id=place_id, door_id=door.id)
        return super(PlaceDetachDoors, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:place attached doors', kwargs={ID: self.kwargs[ID]})