from django.shortcuts import get_object_or_404
from django.urls import reverse

from jba_core.models import Controller, Door
from jba_core.service import ControllerService, DoorService
from jba_ui.common.CommonViews import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from jba_ui.common.model_types import CONTROLLER
from jba_ui.common.view_fields import ID
from jba_ui.forms import ControllerForm, DoorChoiceForm


class ControllerListView(ListView):
    template_name = 'controllers/controller-list.html'
    title = 'Controller list'
    model = Controller
    details_url_name = 'ui:controller details'
    fields = ['id', 'name', 'controller_id']

    def get_queryset(self):
        return ControllerService.get_all()


class ControllerDetailsView(DetailView):
    template_name = 'controllers/controller-details.html'
    fields = ['id', 'name', 'controller_id']
    title = 'Controller details'

    def get_object(self, queryset=None):
        return ControllerService.get(id=self.kwargs[ID])


class ControllerCreateView(CreateView):
    template_name = 'controllers/controller-create.html'
    title = 'Create controller'
    form_class = ControllerForm

    def get_success_url(self):
        return reverse('ui:controller list')


class ControllerUpdateView(UpdateView):
    template_name = 'controllers/controller-update.html'
    form_class = ControllerForm
    title = 'Update controller'

    def get_object(self, queryset=None):
        return ControllerService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:controller details', kwargs={ID: self.kwargs[ID]})


class ControllerDeleteView(DeleteView):
    template_name = 'controllers/controller-delete.html'
    title = 'Delete controller'

    def get_object(self, queryset=None):
        return ControllerService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:controller list')


class AttachedDoorsToControllerView(ListView):
    template_name = 'controllers/controller-attached-doors-list.html'
    title = 'Attached controllers'
    model = Door
    details_url_name = 'ui:door details'
    fields = ['id', 'name', 'access_id']

    def get_queryset(self):
        return ControllerService.get_attached_doors(id=self.kwargs[ID])

    def get_context_data(self, **kwargs):
        context = super(AttachedDoorsToControllerView, self).get_context_data(**kwargs)
        context[ID] = self.kwargs[ID]
        return context


class ControllerAttachDoorView(FormView):
    template_name = 'controllers/controller-attach-door.html'
    title = 'Attach door'
    form_class = DoorChoiceForm
    obj = None

    def get_form_kwargs(self):
        kwargs = super(ControllerAttachDoorView, self).get_form_kwargs()
        kwargs['controller_id'] = self.kwargs[ID]
        return kwargs

    def get_object(self):
        if self.obj is None:
            self.obj = ControllerService.get(id=self.kwargs[ID])
        return self.obj

    def form_valid(self, form: DoorChoiceForm):
        door = form.cleaned_data['door']
        obj = self.get_object()
        obj.doors.add(door)
        obj.save()
        return super(ControllerAttachDoorView, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:controller details', kwargs={ID: self.kwargs[ID]})
