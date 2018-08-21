from django.http import Http404
from django.urls import reverse

from jba_core.models import Role, Person
from jba_core.service import RoleService, AclService
from jba_ui.common.const import ID, ROLE_ID
from jba_ui.common.views import ModelListView, ModelCreateView, ModelDetailsView, ModelUpdateView, ModelDeleteView, \
    AttachedModelToModel, AttachOrDetachModels, RulesView, AddRuleView
from jba_ui.forms import RoleCreateForm, PersonAttachForm, PersonDetachForm, PlaceAllowRuleForRoleForm, \
    PlaceDenyRuleForRoleForm
from jba_ui.tables import RoleTable, PersonTable, RoleACLEntryTable


class RoleList(ModelListView):
    template_name = 'roles/list.html'
    service = RoleService
    title = 'Roles list'
    model = Role
    table_class = RoleTable


class RoleCreate(ModelCreateView):
    template_name = 'roles/create.html'
    form_class = RoleCreateForm
    form_model = 'role'
    title = 'Create role'

    def get_success_url(self):
        return reverse('ui:role details', kwargs={ID: self.object.id})


class RoleDetail(ModelDetailsView):
    template_name = 'roles/details.html'
    fields = ['id', 'name']
    model = Role
    service = RoleService
    title = 'Role\'s details'


class RoleUpdate(ModelUpdateView):
    template_name = 'roles/update.html'
    title = 'Update role'
    form_class = RoleCreateForm
    form_model = 'role'
    service = RoleService

    def get_success_url(self):
        return reverse('ui:role details', kwargs={ID: self.get_obj_id()})


class RoleDelete(ModelDeleteView):
    template_name = 'roles/delete.html'
    form_model = 'role'
    model = Role
    title = 'Delete role'
    service = RoleService

    def get_success_url(self):
        return reverse('ui:role list')


class AttachedPersonsToRole(AttachedModelToModel):
    template_name = 'roles/attached-persons.html'
    model = Person
    table_class = PersonTable

    def get_queryset(self):
        try:
            return RoleService.get_persons(id=self.get_obj_id())
        except:
            raise Http404


class AttachPersonsToRole(AttachOrDetachModels):
    template_name = 'roles/attach-persons.html'
    form_model = 'person'
    title = 'Attach persons'
    form_class = PersonAttachForm
    obj_id_form_name = ROLE_ID

    def get_success_url(self):
        return reverse('ui:role attached persons', kwargs={ID: self.get_obj_id()})


class DetachPersonsFromRole(AttachOrDetachModels):
    template_name = 'roles/detach-persons.html'
    form_model = 'person'
    title = 'Detach persons'
    form_class = PersonDetachForm
    obj_id_form_name = ROLE_ID

    def get_success_url(self):
        return reverse('ui:role attached persons', kwargs={ID: self.get_obj_id()})


class RoleAclsRules(RulesView):
    template_name = 'roles/acl-rules.html'
    title = 'Allowed places'
    table_class = RoleACLEntryTable

    def get_queryset(self):
        try:
            return AclService.get_role_acls(role_id=self.get_obj_id())
        except:
            raise Http404


class RoleAllowPlaces(AddRuleView):
    template_name = 'roles/acl-allow.html'
    title = 'Allow places'
    form_class = PlaceAllowRuleForRoleForm
    form_model = 'place'
    obj_id_context_name = ROLE_ID

    def get_success_url(self):
        return reverse('ui:role acl rules', kwargs={ID: self.get_obj_id()})


class RoleDenyPlaces(AddRuleView):
    template_name = 'roles/acl-deny.html'
    title = 'Deny places'
    form_class = PlaceDenyRuleForRoleForm
    form_model = 'place'
    obj_id_context_name = ROLE_ID

    def get_success_url(self):
        return reverse('ui:role acl rules', kwargs={ID: self.get_obj_id()})
