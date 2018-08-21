from django.http import Http404
from django.urls import reverse

from jba_core.models import Place
from jba_core.service import PlaceService
from jba_ui.common.const import ID, NAME, PLACE, DOOR, PLACE_ID
from jba_ui.common.views import ModelListView, ModelCreateView, ModelDetailsView, ModelUpdateView, ModelDeleteView, \
    AttachedModelToModel, AttachOrDetachModels
from jba_ui.forms import PlaceCreateForm, DoorAttachToPlaceForm, DoorDetachPlaceForm
from jba_ui.tables import PlaceTable, DoorTable


class PlaceList(ModelListView):
    template_name = 'places/list.html'
    title = 'Places list'
    model = Place
    table_class = PlaceTable
    service = PlaceService


class PlaceCreate(ModelCreateView):
    template_name = 'places/create.html'
    title = 'Create place'
    form_model = PLACE
    form_class = PlaceCreateForm

    def get_success_url(self):
        return reverse('ui:place details', kwargs={ID: self.object.id})


class PlaceDetails(ModelDetailsView):
    template_name = 'places/details.html'
    title = 'Place\'es details'
    fields = [ID, NAME]
    service = PlaceService


class PlaceUpdate(ModelUpdateView):
    template_name = 'places/update.html'
    form_class = PlaceCreateForm
    form_model = PLACE
    title = 'Update place'
    service = PlaceService

    def get_success_url(self):
        return reverse('ui:place details', kwargs={ID: self.get_object().id})


class PlaceDelete(ModelDeleteView):
    template_name = 'places/delete.html'
    title = 'Delete place'
    form_model = PLACE
    service = PlaceService

    def get_success_url(self):
        return reverse('ui:place list')


class PlaceAttachedDoors(AttachedModelToModel):
    template_name = 'places/attached-doors.html'
    table_class = DoorTable
    title = 'Attached doors'

    def get_queryset(self):
        try:
            return PlaceService.get_doors(id=self.kwargs[ID])
        except:
            raise Http404


class PlaceAttachDoors(AttachOrDetachModels):
    template_name = 'places/attach-doors.html'
    title = 'Attach doors'
    form_model = DOOR
    form_class = DoorAttachToPlaceForm
    obj_id_form_name = PLACE_ID

    def get_success_url(self):
        return reverse('ui:place attached doors', kwargs={ID: self.get_obj_id()})


class PlaceDetachDoors(AttachOrDetachModels):
    template_name = 'places/detach-doors.html'
    title = 'Detach doors'
    form_model = DOOR
    form_class = DoorDetachPlaceForm
    obj_id_form_name = PLACE_ID

    def get_success_url(self):
        return reverse('ui:place attached doors', kwargs={ID: self.get_obj_id()})
