from django.urls import reverse
from django.views.generic import DeleteView, ListView, CreateView, DetailView, UpdateView, FormView
from django_tables2 import SingleTableView

from jba_core.models import Role
from jba_ui.common.mixins import DetailsUrlMixin, TitleMixin, ModelFieldsMixin, IdToContextMixin
from jba_core.service import RoleService, PersonService
from jba_ui.common.view_fields import ID, NAME
from jba_ui.forms import RoleForm, PersonMultipleChoiceForm
from jba_ui.tables import RoleTable


class RoleList(SingleTableView, TitleMixin, ModelFieldsMixin):
    template_name = 'roles/list.html'
    title = 'Role list'
    model = Role
    table_class = RoleTable

    def get_queryset(self):
        return RoleService.get_all()


class RoleCreate(CreateView, TitleMixin):
    template_name = 'roles/role-create.html'
    form_class = RoleForm
    title = 'Create Role'

    def get_success_url(self):
        return reverse('ui:role list')


class RoleDetail(DetailView, ModelFieldsMixin, TitleMixin, IdToContextMixin):
    template_name = 'roles/role-details.html'
    fields = ['id', 'name']
    title = 'Role details'

    def get_object(self, queryset=None):
        return RoleService.get(id=self.kwargs[ID])


class RoleUpdate(UpdateView, TitleMixin):
    template_name = 'roles/role-update.html'
    title = 'Update role'
    form_class = RoleForm

    def get_object(self, queryset=None):
        return RoleService.get(self.kwargs[ID])

    def form_valid(self, form: RoleForm):
        RoleService.update(id=self.kwargs[ID], name=form.cleaned_data[NAME])
        return super(RoleUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:role details', kwargs={ID: self.kwargs[ID]})


class RoleDelete(DeleteView, TitleMixin, IdToContextMixin):
    template_name = 'roles/role-delete.html'
    model = Role
    title = 'Delete role'

    def get_object(self, queryset=None):
        return RoleService.get(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:role list')


class AttachPersonsToRole(FormView, TitleMixin):
    template_name = 'roles/role-attach-persons.html'
    title = 'Attach Role'
    form_class = PersonMultipleChoiceForm
    role_id = None

    def get_role_id(self):
        if not self.role_id:
            self.role_id = self.kwargs[ID]
        return self.role_id

    def get_form_kwargs(self):
        kwargs = super(AttachPersonsToRole, self).get_form_kwargs()
        kwargs['role_id'] = self.get_role_id()
        return kwargs

    def form_valid(self, form: PersonMultipleChoiceForm):
        persons = form.cleaned_data['person']
        for person in persons:
            PersonService.attach_role(person_id=person.id, role_id=self.get_role_id())
        return super(AttachPersonsToRole, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:person details', kwargs={ID: self.get_role_id()})
