from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django_tables2 import SingleTableView

from jba_core.models import Door
from jba_core.service import DoorService, ControllerService, PlaceService
from jba_ui.common.mixins import TitleMixin, ModelFieldsMixin, IdToContextMixin
from jba_ui.common.const import ID
from jba_ui.forms import DoorCreateForm, ControllerAttachForm, ControllerDetachForm
from jba_ui.forms.place import PlaceAttachForm, PlaceDetachForm
from jba_ui.tables import DoorTable, ControllerTable, PlaceTable


class DoorList(SingleTableView, TitleMixin):
    template_name = 'doors/list.html'
    title = 'Doors list'
    model = Door
    table_class = DoorTable

    def get_queryset(self):
        return DoorService.get_all()


class DoorDetails(DetailView, TitleMixin, ModelFieldsMixin, IdToContextMixin):
    template_name = 'doors/details.html'
    fields = ['id', 'name', 'access_id']
    title = 'Door details'

    def get_object(self, queryset=None):
        try:
            return DoorService.get(id=self.kwargs[ID])
        except:
            raise Http404


class DoorCreate(CreateView, TitleMixin):
    template_name = 'doors/create.html'
    title = 'Create door'
    form_class = DoorCreateForm

    def form_valid(self, form: DoorCreateForm):
        name = form.cleaned_data['name']
        access_id = form.cleaned_data['access_id']
        DoorService.create(name=name, access_id=access_id)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:door list')


class DoorUpdate(UpdateView, TitleMixin, IdToContextMixin):
    template_name = 'doors/update.html'
    form_class = DoorCreateForm
    title = 'Update door'
    obj = None

    def get_object(self, queryset=None):
        if self.obj is None:
            self.obj = DoorService.get(id=self.kwargs[ID])
        return self.obj

    def form_valid(self, form: DoorCreateForm):
        name = form.cleaned_data['name']
        access_id = form.cleaned_data['access_id']
        DoorService.update(id=self.get_object().id, name=name, access_id=access_id)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:door details', kwargs={ID: self.kwargs[ID]})


class DoorDelete(DeleteView, TitleMixin, IdToContextMixin):
    template_name = 'doors/delete.html'
    title = 'Delete door'
    obj = None

    def get_object(self, queryset=None):
        if self.obj is None:
            self.obj = DoorService.get(id=self.kwargs[ID])
        return self.obj

    def delete(self, request, *args, **kwargs):
        DoorService.delete(id=self.get_object().id)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:door list')


class DoorAttachedControllers(SingleTableView, IdToContextMixin, TitleMixin):
    template_name = 'doors/attached-controllers.html'
    title = 'Attached controllers'
    table_class = ControllerTable

    def get_queryset(self):
        return DoorService.get_attached_controllers(id=self.kwargs[ID])


class DoorAttachControllers(FormView, IdToContextMixin, TitleMixin):
    template_name = 'doors/attach-controllers.html'
    title = 'Attach controllers'
    form_class = ControllerAttachForm

    def get_form_kwargs(self):
        kwargs = super(DoorAttachControllers, self).get_form_kwargs()
        kwargs['door_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        controllers = form.cleaned_data['controllers']
        door_id = self.kwargs[ID]
        for controller in controllers:
            ControllerService.attach_door(controller_id=controller.id, door_id=door_id)
        return super(DoorAttachControllers, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:door attached controllers', kwargs={ID: self.kwargs[ID]})


class DoorDetachControllers(FormView, IdToContextMixin, TitleMixin):
    template_name = 'doors/detach-controllers.html'
    title = 'Detach controllers'
    form_class = ControllerDetachForm

    def get_form_kwargs(self):
        kwargs = super(DoorDetachControllers, self).get_form_kwargs()
        kwargs['door_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        controllers = form.cleaned_data['controllers']
        door_id = self.kwargs[ID]
        for controller in controllers:
            ControllerService.detach_door(controller_id=controller.id, door_id=door_id)
        return super(DoorDetachControllers, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:door attached controllers', kwargs={ID: self.kwargs[ID]})


class DoorAttachedPlaces(SingleTableView, IdToContextMixin, TitleMixin):
    template_name = 'doors/attached-places.html'
    title = 'Attached places'
    table_class = PlaceTable

    def get_queryset(self):
        return DoorService.get_attached_places(id=self.kwargs[ID])


class DoorAttachPlaces(FormView, IdToContextMixin, TitleMixin):
    template_name = 'doors/attach-places.html'
    title = 'Attach places'
    form_class = PlaceAttachForm

    def get_form_kwargs(self):
        kwargs = super(DoorAttachPlaces, self).get_form_kwargs()
        kwargs['door_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        places = form.cleaned_data['places']
        door_id = self.kwargs[ID]
        for place in places:
            PlaceService.attach_door(place_id=place.id, door_id=door_id)
        return super(DoorAttachPlaces, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:door attached places', kwargs={ID: self.kwargs[ID]})


class DoorDetachPlaces(FormView, IdToContextMixin, TitleMixin):
    template_name = 'doors/detach-places.html'
    title = 'Detach place'
    form_class = PlaceDetachForm

    def get_form_kwargs(self):
        kwargs = super(DoorDetachPlaces, self).get_form_kwargs()
        kwargs['door_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        places = form.cleaned_data['places']
        door_id = self.kwargs[ID]
        for place in places:
            PlaceService.detach_door(place_id=place.id, door_id=door_id)
        return super(DoorDetachPlaces, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:door attached places', kwargs={ID: self.kwargs[ID]})
