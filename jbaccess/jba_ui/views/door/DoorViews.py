from django.http import Http404
from django.urls import reverse

from jba_core.models import Door
from jba_core.service import DoorService
from jba_ui.common.const import ID
from jba_ui.common.views import ModelListView, ModelCreateView, ModelDetailsView, ModelUpdateView, ModelDeleteView, \
    AttachedModelToModel, AttachOrDetachModels
from jba_ui.forms import DoorCreateForm, ControllerAttachForm, ControllerDetachForm, DoorUpdateForm
from jba_ui.forms.place import PlaceAttachForm, PlaceDetachForm
from jba_ui.tables import DoorTable, ControllerTable, PlaceTable


class DoorList(ModelListView):
    template_name = 'doors/list.html'
    title = 'Doors list'
    model = Door
    table_class = DoorTable
    service = DoorService


class DoorDetails(ModelDetailsView):
    template_name = 'doors/details.html'
    fields = ['id', 'name', 'access_id']
    model = Door
    title = 'Door details'
    service = DoorService


class DoorCreate(ModelCreateView):
    template_name = 'doors/create.html'
    title = 'Create door'
    form_model = 'door'
    form_class = DoorCreateForm

    def get_success_url(self):
        return reverse('ui:door details', kwargs={ID: self.object.id})


class DoorUpdate(ModelUpdateView):
    template_name = 'doors/update.html'
    title = 'Update door'
    form_class = DoorUpdateForm
    form_model = 'door'
    service = DoorService

    def get_success_url(self):
        return reverse('ui:door details', kwargs={ID: self.get_obj_id()})


class DoorDelete(ModelDeleteView):
    template_name = 'doors/delete.html'
    title = 'Delete door'
    model = Door
    form_model = 'door'
    service = DoorService

    def get_success_url(self):
        return reverse('ui:door list')


class DoorAttachedControllers(AttachedModelToModel):
    template_name = 'doors/attached-controllers.html'
    title = 'Attached controllers'
    table_class = ControllerTable

    def get_queryset(self):
        try:
            return DoorService.get_attached_controllers(id=self.kwargs[ID])
        except:
            raise Http404


class DoorAttachControllers(AttachOrDetachModels):
    template_name = 'doors/attach-controllers.html'
    title = 'Attach controllers'
    form_class = ControllerAttachForm
    form_model = 'controller'
    obj_id_form_name = 'door_id'

    def get_success_url(self):
        return reverse('ui:door attached controllers', kwargs={ID: self.get_obj_id()})


class DoorDetachControllers(AttachOrDetachModels):
    template_name = 'doors/detach-controllers.html'
    title = 'Detach controllers'
    form_class = ControllerDetachForm
    form_model = 'controller'
    obj_id_form_name = 'door_id'

    def get_success_url(self):
        return reverse('ui:door attached controllers', kwargs={ID: self.get_obj_id()})


class DoorAttachedPlaces(AttachedModelToModel):
    template_name = 'doors/attached-places.html'
    title = 'Attached places'
    table_class = PlaceTable

    def get_queryset(self):
        try:
            return DoorService.get_attached_places(id=self.kwargs[ID])
        except:
            raise Http404


class DoorAttachPlaces(AttachOrDetachModels):
    template_name = 'doors/attach-places.html'
    title = 'Attach places'
    form_class = PlaceAttachForm
    form_model = 'place'
    obj_id_form_name = 'door_id'

    def get_success_url(self):
        return reverse('ui:door attached places', kwargs={ID: self.get_obj_id()})


class DoorDetachPlaces(AttachOrDetachModels):
    template_name = 'doors/detach-places.html'
    title = 'Detach place'
    form_class = PlaceDetachForm
    form_model = 'place'
    obj_id_form_name = 'door_id'

    def get_success_url(self):
        return reverse('ui:door attached places', kwargs={ID: self.get_obj_id()})
