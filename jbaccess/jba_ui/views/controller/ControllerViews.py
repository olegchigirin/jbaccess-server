from django.http import Http404
from django.urls import reverse
from django_tables2 import SingleTableView

from jba_core.models import Controller
from jba_core.service import ControllerService, AclService
from jba_ui.common.const import ID
from jba_ui.common.mixins import TitleMixin, IdToContextMixin, ReturnUrlMixin
from jba_ui.common.views import ModelListView, ModelCreateView, ModelDetailsView, ModelUpdateView, ModelDeleteView, \
    AttachedModelToModel, AttachOrDetachModels
from jba_ui.forms import ControllerCreateForm, DoorDetachControllerForm, DoorAttachToControllerForm
from jba_ui.tables import ControllerTable, DoorTable, ControllerResolveTable


class ControllerList(ModelListView):
    template_name = 'controllers/list.html'
    title = 'Controller list'
    model = Controller
    table_class = ControllerTable
    service = ControllerService


class ControllerCreate(ModelCreateView):
    template_name = 'controllers/create.html'
    title = 'Create controller'
    form_class = ControllerCreateForm
    form_model = 'controller'

    def get_success_url(self):
        return reverse('ui:controller details', kwargs={ID: self.object.id})


class ControllerDetails(ModelDetailsView):
    template_name = 'controllers/details.html'
    title = 'Controller details'
    fields = ['id', 'name', 'controller_id']
    model = Controller
    service = ControllerService


class ControllerUpdate(ModelUpdateView):
    template_name = 'controllers/update.html'
    form_class = ControllerCreateForm
    form_model = 'controller'
    title = 'Update controller'
    service = ControllerService

    def get_success_url(self):
        return reverse('ui:controller details', kwargs={ID: self.get_obj_id()})


class ControllerDelete(ModelDeleteView):
    template_name = 'controllers/delete.html'
    title = 'Delete controller'
    model = Controller
    form_model = 'controller'
    service = ControllerService

    def get_success_url(self):
        return reverse('ui:controller list')


class ControllerAttachedDoors(AttachedModelToModel):
    template_name = 'controllers/attached-doors.html'
    title = 'Attached doors'
    table_class = DoorTable

    def get_queryset(self):
        try:
            return ControllerService.get_doors(id=self.get_obj_id())
        except:
            raise Http404


class ControllerAttachDoors(AttachOrDetachModels):
    template_name = 'controllers/attach-doors.html'
    title = 'Attach doors'
    form_model = 'door'
    form_class = DoorAttachToControllerForm
    obj_id_form_name = 'controller_id'

    def get_success_url(self):
        return reverse('ui:controller attached doors', kwargs={ID: self.get_obj_id()})


class ControllerDetachDoors(AttachOrDetachModels):
    template_name = 'controllers/detach-doors.html'
    title = 'Attach doors'
    form_class = DoorDetachControllerForm
    form_model = 'door'
    obj_id_form_name = 'controller_id'

    def get_success_url(self):
        return reverse('ui:controller attached doors', kwargs={ID: self.kwargs[ID]})


class ControllerResolveAcls(SingleTableView, ReturnUrlMixin, TitleMixin, IdToContextMixin):
    template_name = 'controllers/resolve-acls.html'
    title = 'Resolve controller'
    table_class = ControllerResolveTable
    queryset = None

    def get_queryset(self):
        if self.queryset is None:
            controller = ControllerService.get(id=self.get_obj_id())
            self.queryset = AclService.resolve_acls_by_controller(controller_id=controller.controller_id)
        return self.queryset

    def get_table_data(self):
        data = []
        for type, key, door, pattern in self.get_queryset():
            data.append({
                'type': type,
                'key': key,
                'door': door,
                'pattern': pattern
            })
        return data
