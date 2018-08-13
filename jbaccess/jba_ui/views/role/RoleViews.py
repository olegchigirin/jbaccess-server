from django.urls import reverse
from django.views.generic import DeleteView, ListView, CreateView, DetailView, UpdateView, FormView
from django_tables2 import SingleTableView

from jba_core.exceptions import AclAlreadyAdded
from jba_core.models import Role, Person
from jba_ui.common.mixins import DetailsUrlMixin, TitleMixin, ModelFieldsMixin, IdToContextMixin
from jba_core.service import RoleService, PersonService, AclService
from jba_ui.common.const import ID, NAME, PLACES
from jba_ui.common.views import AllowedRulesView, AddAllowRuleView, AddDenyRuleView
from jba_ui.forms import RoleCreateForm, PersonAttachForm, PersonDetachForm, PlacesForm
from jba_ui.tables import RoleTable, PersonTable, RoleACLEntryTable


class RoleList(SingleTableView, TitleMixin, ModelFieldsMixin):
    template_name = 'roles/list.html'
    title = 'Role list'
    model = Role
    table_class = RoleTable

    def get_queryset(self):
        return RoleService.get_all()


class RoleCreate(CreateView, TitleMixin):
    template_name = 'roles/create.html'
    form_class = RoleCreateForm
    title = 'Create Role'

    def get_success_url(self):
        return reverse('ui:role list')


class RoleDetail(DetailView, ModelFieldsMixin, TitleMixin, IdToContextMixin):
    template_name = 'roles/details.html'
    fields = ['id', 'name']
    title = 'Role details'

    def get_object(self, queryset=None):
        return RoleService.get(id=self.kwargs[ID])


class RoleUpdate(UpdateView, TitleMixin):
    template_name = 'roles/update.html'
    title = 'Update role'
    form_class = RoleCreateForm

    def get_object(self, queryset=None):
        return RoleService.get(self.kwargs[ID])

    def form_valid(self, form: RoleCreateForm):
        RoleService.update(id=self.kwargs[ID], name=form.cleaned_data[NAME])
        return super(RoleUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:role details', kwargs={ID: self.kwargs[ID]})


class RoleDelete(DeleteView, TitleMixin, IdToContextMixin):
    template_name = 'roles/delete.html'
    model = Role
    title = 'Delete role'

    def get_object(self, queryset=None):
        return RoleService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:role list')


class AttachedPersonsToRole(SingleTableView, TitleMixin, IdToContextMixin):
    template_name = 'roles/attached-persons.html'
    model = Person
    table_class = PersonTable

    def get_queryset(self):
        return RoleService.get_persons(id=self.kwargs[ID])


class AttachPersonsToRole(FormView, TitleMixin, IdToContextMixin):
    template_name = 'roles/attach-persons.html'
    title = 'Attach Role'
    form_class = PersonAttachForm

    def get_form_kwargs(self):
        kwargs = super(AttachPersonsToRole, self).get_form_kwargs()
        kwargs['role_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        persons = form.cleaned_data['persons']
        for person in persons:
            PersonService.attach_role(person_id=person.id, role_id=self.kwargs[ID])
        return super(AttachPersonsToRole, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:role attached persons', kwargs={ID: self.kwargs[ID]})


class DetachPersonsFromRole(FormView, TitleMixin, IdToContextMixin):
    template_name = 'roles/detach-persons.html'
    title = 'Detach persons'
    form_class = PersonDetachForm

    def get_form_kwargs(self):
        kwargs = super(DetachPersonsFromRole, self).get_form_kwargs()
        kwargs['role_id'] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        role_id = self.kwargs[ID]
        persons = form.cleaned_data['persons']
        for person in persons:
            PersonService.detach_role(person_id=person.id, role_id=role_id)
        return super(DetachPersonsFromRole, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:role attached persons', kwargs={ID: self.kwargs[ID]})


class RoleAllowedPlaces(AllowedRulesView):
    template_name = 'roles/acl-rules.html'
    title = 'Allowed places'
    table_class = RoleACLEntryTable

    def get_queryset(self):
        return AclService.get_role_acls(role_id=self.kwargs[ID])


class RoleAllowPlaces(AddAllowRuleView):
    template_name = 'roles/acl-allow.html'
    title = 'Allow places for role'
    form_class = PlacesForm

    def form_valid(self, form):
        places = form.cleaned_data[PLACES]
        role_id = self.kwargs[ID]
        for place in places:
            try:
                AclService.role_allow_place(role_id=role_id, place_id=place.id)
            except AclAlreadyAdded:
                continue
        return super(RoleAllowPlaces, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:role acl rules', kwargs={ID: self.kwargs[ID]})


class RoleDenyPlaces(AddDenyRuleView):
    template_name = 'roles/acl-deny.html'
    title = 'Deny places for role'
    form_class = PlacesForm

    def form_valid(self, form):
        places = form.cleaned_data[PLACES]
        role_id = self.kwargs[ID]
        for place in places:
            try:
                AclService.role_deny_place(role_id=role_id, place_id=place.id)
            except AclAlreadyAdded:
                continue
        return super(RoleDenyPlaces, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:role acl rules', kwargs={ID: self.kwargs[ID]})
