from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from django_tables2 import SingleTableView

from jba_core.models import Person
from jba_core.service import PersonService, KeyService
from jba_ui.common.mixins import DetailsUrlMixin, TitleMixin, ModelFieldsMixin, IdToContextMixin
from jba_ui.common.view_fields import ID
from jba_ui.forms import PersonForm, AttachRolesMultiChoiceForm, DetachRolesMultiChoiceForm
from jba_ui.forms.key import KeyAttachMultipleChoiceForm
from jba_ui.tables import PersonTable, RoleTable, KeyTable


class PersonList(SingleTableView, TitleMixin, DetailsUrlMixin):
    template_name = 'personnel/list.html'
    model = Person
    details_url_name = 'ui:person details'
    title = 'Person list'
    table_class = PersonTable

    def get_queryset(self):
        return PersonService.get_all()


class PersonCreate(CreateView, TitleMixin):
    template_name = 'personnel/create.html'
    form_class = PersonForm
    title = 'Create person'

    def get_success_url(self):
        return reverse('ui:person list')


class PersonDetail(DetailView, TitleMixin, ModelFieldsMixin, IdToContextMixin):
    template_name = 'personnel/detail.html'
    model = Person
    fields = ['id', 'name']
    title = 'Person details'

    def get_object(self, queryset=None):
        return PersonService.get(self.kwargs[ID])


class PersonUpdate(UpdateView, TitleMixin, IdToContextMixin):
    template_name = 'personnel/update.html'
    form_class = PersonForm
    title = 'Person update'

    def get_object(self, queryset=None):
        return PersonService.get(self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:person details', kwargs={ID: self.kwargs[ID]})


class PersonDelete(DeleteView, TitleMixin, IdToContextMixin):
    template_name = 'personnel/delete.html'
    model = Person
    title = 'Delete person'

    def get_object(self, queryset=None):
        return PersonService.get(self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:person list')


class RolesAttachedToPerson(SingleTableView, TitleMixin, IdToContextMixin):
    template_name = 'personnel/attached-roles.html'
    title = 'Attached roles'
    table_class = RoleTable

    def get_queryset(self):
        return PersonService.get_roles(id=self.kwargs[ID])


class AttachRolesToPerson(FormView, TitleMixin, IdToContextMixin):
    template_name = 'personnel/attach-roles.html'
    title = 'Attach roles'
    form_class = AttachRolesMultiChoiceForm

    def get_form_kwargs(self):
        kwargs = super(AttachRolesToPerson, self).get_form_kwargs()
        kwargs['person_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form: AttachRolesMultiChoiceForm):
        roles = form.cleaned_data['roles']
        person_id = self.kwargs[ID]
        for role in roles:
            PersonService.attach_role(person_id=person_id, role_id=role.id)
        return super(AttachRolesToPerson, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:person attached roles', kwargs={ID: self.kwargs[ID]})


class DetachRolesFromPerson(FormView, TitleMixin, IdToContextMixin):
    template_name = 'personnel/detach-role.html'
    title = 'Detach roles'
    form_class = DetachRolesMultiChoiceForm

    def get_form_kwargs(self):
        kwargs = super(DetachRolesFromPerson, self).get_form_kwargs()
        kwargs['person_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        person_id = self.kwargs[ID]
        roles = form.cleaned_data['roles']
        for role in roles:
            PersonService.detach_role(person_id=person_id, role_id=role.id)
        return super(DetachRolesFromPerson, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:person attached roles', kwargs={ID: self.kwargs[ID]})


class AttachedKeysToPerson(SingleTableView, TitleMixin, IdToContextMixin):
    template_name = 'personnel/attached-keys.html'
    title = 'Attached keys'
    table_class = KeyTable

    def get_queryset(self):
        return PersonService.get_keys(id=self.kwargs[ID])


class AttachKeysToPerson(FormView, TitleMixin, IdToContextMixin):
    template_name = 'personnel/attach-keys.html'
    title = 'Attach keys'
    form_class = KeyAttachMultipleChoiceForm

    def get_form_kwargs(self):
        kwargs = super(AttachKeysToPerson, self).get_form_kwargs()
        kwargs['person_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        person = PersonService.get(id=self.kwargs[ID])
        keys = form.cleaned_data['keys']
        for key in keys:
            key.person = person
            key.save()
        return super(AttachKeysToPerson, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:person attached keys', kwargs={ID: self.kwargs[ID]})
