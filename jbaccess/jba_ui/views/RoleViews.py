from django.urls import reverse
from django.views.generic import DeleteView

from jba_core.models import Role
from jba_core.service import RoleService
from jba_ui.forms import RoleForm
from jba_ui.views.CustomViews import CustomCreateView, CustomDetailView, CustomListView, CustomUpdateView


class RoleListView(CustomListView):
    template_name = 'roles/role-list.html'
    title = 'Role list'
    fields = ['id', 'name']
    model = Role

    def get_queryset(self):
        return RoleService.get_all()


class RoleCreateView(CustomCreateView):
    template_name = 'roles/role-create.html'
    form_class = RoleForm
    title = 'Create Role'

    def get_success_url(self):
        return reverse('ui:role list')


class RoleDetailView(CustomDetailView):
    template_name = 'roles/role-details.html'
    describe_fields = ['id', 'name']
    title = 'Role details'

    def get_object(self, queryset=None):
        return RoleService.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(RoleDetailView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        return context


class RoleUpdateView(CustomUpdateView):
    template_name = 'roles/role-update.html'
    title = 'Update role'
    form_class = RoleForm

    def get_object(self, queryset=None):
        return RoleService.get(self.kwargs['id'])

    def form_valid(self, form: RoleForm):
        RoleService.update(id=self.kwargs['id'], name=form.cleaned_data['name'])
        return super(RoleUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:role details', kwargs={'id': self.kwargs['id']})


class RoleDeleteView(DeleteView):
    template_name = 'roles/role-delete.html'
    model = Role
    title = 'Delete role'

    def get_title(self):
        return self.title

    def get_object(self, queryset=None):
        return RoleService.get(id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(RoleDeleteView, self).get_context_data(**kwargs)
        context['id'] = self.kwargs['id']
        context['title'] = self.get_title()
        return context

    def get_success_url(self):
        return reverse('ui:role list')
