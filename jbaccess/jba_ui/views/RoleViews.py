from django.urls import reverse
from django.views.generic import DeleteView

from jba_core.models import Role, Person
from jba_core.service import RoleService, PersonService
from jba_ui.common.model_types import ROLE, PERSON
from jba_ui.common.view_fields import ID, NAME, PERSON_ID
from jba_ui.forms import RoleForm, AttachRoleToPersonForm
from jba_ui.common.CommonViews import CreateView, DetailView, UpdateView, ListView, FormView


class RoleListView(ListView):
    template_name = 'roles/role-list.html'
    title = 'Role list'
    fields = ['id', 'name']
    model_name = ROLE
    model = Role

    def get_queryset(self):
        return RoleService.get_all()


class RoleCreateView(CreateView):
    template_name = 'roles/role-create.html'
    form_class = RoleForm
    title = 'Create Role'

    def get_success_url(self):
        return reverse('ui:role list')


class RoleDetailView(DetailView):
    template_name = 'roles/role-details.html'
    fields = ['id', 'name']
    title = 'Role details'

    def get_object(self, queryset=None):
        return RoleService.get(id=self.kwargs[ID])

    def get_context_data(self, **kwargs):
        context = super(RoleDetailView, self).get_context_data(**kwargs)
        context[ID] = self.kwargs[ID]
        return context


class RoleUpdateView(UpdateView):
    template_name = 'roles/role-update.html'
    title = 'Update role'
    form_class = RoleForm

    def get_object(self, queryset=None):
        return RoleService.get(self.kwargs[ID])

    def form_valid(self, form: RoleForm):
        RoleService.update(id=self.kwargs[ID], name=form.cleaned_data[NAME])
        return super(RoleUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:role details', kwargs={ID: self.kwargs[ID]})


class RoleDeleteView(DeleteView):
    template_name = 'roles/role-delete.html'
    model = Role
    title = 'Delete role'

    def get_title(self):
        return self.title

    def get_object(self, queryset=None):
        return RoleService.get(id=self.kwargs[ID])

    def get_context_data(self, **kwargs):
        context = super(RoleDeleteView, self).get_context_data(**kwargs)
        context[ID] = self.kwargs[ID]
        return context

    def get_success_url(self):
        return reverse('ui:role list')


class AttachRoleToPersonView(FormView):
    template_name = 'roles/attach-role-to-person.html'
    title = 'Attach Role'
    form_class = AttachRoleToPersonForm

    def form_valid(self, form: AttachRoleToPersonForm):
        person: Person = form.cleaned_data[PERSON]
        role = RoleService.get(id=self.kwargs[ID])
        person.roles.add(role)
        person.save()
        self.kwargs[PERSON_ID] = person.id
        return super(AttachRoleToPersonView, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:person details', kwargs={ID: self.kwargs[PERSON_ID]})


class AttachedRolesToPersonView(ListView):
    template_name = 'roles/roles-attached-to-person.html'
    model = Role
    model_name = ROLE
    title = 'Attached roles'
    fields = ['id', 'name']

    def get_queryset(self):
        return PersonService.get_roles(id=self.kwargs[ID])

    def get_context_data(self, **kwargs):
        context = super(AttachedRolesToPersonView, self).get_context_data(**kwargs)
        context[ID] = self.kwargs[ID]
        return context

