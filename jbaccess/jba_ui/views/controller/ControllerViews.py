from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, FormView
from django_tables2 import SingleTableView

from jba_core.models import Controller
from jba_core.service import ControllerService
from jba_ui.common.mixins import TitleMixin, ModelFieldsMixin, IdToContextMixin
from jba_ui.common.const import ID
from jba_ui.forms import ControllerCreateForm, DoorAttachForm, DoorDetachForm
from jba_ui.tables import ControllerTable, DoorTable


class ControllerList(SingleTableView, TitleMixin):
    template_name = 'controllers/list.html'
    title = 'Controller list'
    model = Controller
    table_class = ControllerTable

    def get_queryset(self):
        return ControllerService.get_all()


class ControllerCreate(CreateView, TitleMixin):
    template_name = 'controllers/create.html'
    title = 'Create controller'
    form_class = ControllerCreateForm

    def form_valid(self, form: ControllerCreateForm):
        ControllerService.create(
            name=form.cleaned_data['name'],
            controller_id=form.cleaned_data['controller_id']
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:controller list')


class ControllerDetails(DetailView, TitleMixin, ModelFieldsMixin, IdToContextMixin):
    template_name = 'controllers/details.html'
    fields = ['id', 'name', 'controller_id']
    title = 'Controller details'

    def get_object(self, queryset=None):
        return ControllerService.get(id=self.kwargs[ID])


class ControllerUpdate(UpdateView, TitleMixin, IdToContextMixin):
    template_name = 'controllers/update.html'
    form_class = ControllerCreateForm
    title = 'Update controller'
    obj = None

    def get_object(self, queryset=None):
        if self.obj is None:
            self.obj = ControllerService.get(id=self.kwargs[ID])
        return self.obj

    def form_valid(self, form: ControllerCreateForm):
        ControllerService.update(
            id=self.get_object().id,
            name=form.cleaned_data['name'],
            controller_id=form.cleaned_data['controller_id']
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:controller details', kwargs={ID: self.kwargs[ID]})


class ControllerDelete(DeleteView, TitleMixin, IdToContextMixin):
    template_name = 'controllers/delete.html'
    title = 'Delete controller'
    obj = None

    def get_object(self, queryset=None):
        if self.obj is None:
            self.obj = ControllerService.get(id=self.kwargs[ID])
        return self.obj

    def delete(self, request, *args, **kwargs):
        ControllerService.delete(id=self.get_object().id)
        return super(ControllerDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('ui:controller list')


class ControllerAttachedDoors(SingleTableView, TitleMixin, IdToContextMixin):
    template_name = 'controllers/attached-doors.html'
    title = 'Attached doors'
    table_class = DoorTable

    def get_queryset(self):
        return ControllerService.get_doors(id=self.kwargs[ID])


class ControllerAttachDoors(FormView, TitleMixin, IdToContextMixin):
    template_name = 'controllers/attach-doors.html'
    title = 'Attach doors'
    form_class = DoorAttachForm

    def get_form_kwargs(self):
        kwargs = super(ControllerAttachDoors, self).get_form_kwargs()
        kwargs['controller_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        controller_id = self.kwargs[ID]
        doors = form.cleaned_data['doors']
        for door in doors:
            ControllerService.attach_door(controller_id=controller_id, door_id=door.id)
        return super(ControllerAttachDoors, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:controller attached doors', kwargs={ID: self.kwargs[ID]})


class ControllerDetachDoors(FormView, TitleMixin, IdToContextMixin):
    template_name = 'controllers/detach-doors.html'
    title = 'Attach doors'
    form_class = DoorDetachForm

    def get_form_kwargs(self):
        kwargs = super(ControllerDetachDoors, self).get_form_kwargs()
        kwargs['controller_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        controller_id = self.kwargs[ID]
        doors = form.cleaned_data['doors']
        for door in doors:
            ControllerService.detach_door(controller_id=controller_id, door_id=door.id)
        return super(ControllerDetachDoors, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:controller attached doors', kwargs={ID: self.kwargs[ID]})
