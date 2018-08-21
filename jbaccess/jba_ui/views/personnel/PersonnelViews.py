from django.http import Http404
from django.urls import reverse

from jba_core.models import Person
from jba_core.service import PersonService, AclService
from jba_ui.common.const import ID, PERSON_ID
from jba_ui.common.mixins import IdToContextMixin
from jba_ui.common.views import ModelListView, ModelCreateView, ModelDetailsView, ModelUpdateView, ModelDeleteView, \
    AttachedModelToModel, AttachOrDetachModels, RulesView, AddRuleView
from jba_ui.forms import PersonCreateForm, RoleAttachForm, RoleDetachForm, PlaceAllowRuleForPersonForm, \
    PlaceDenyRuleForPersonForm, KeyCreateForPersonForm
from jba_ui.forms.personnel import PersonUpdateForm
from jba_ui.tables import PersonTable, RoleTable, KeyTable, PersonACLEntryTable


class PersonList(ModelListView):
    template_name = 'personnel/list.html'
    model = Person
    title = 'Persons list'
    table_class = PersonTable
    service = PersonService


class PersonCreate(ModelCreateView):
    template_name = 'personnel/create.html'
    form_class = PersonCreateForm
    form_model = 'person'
    title = 'Create person'

    def get_success_url(self):
        return reverse('ui:person details', kwargs={ID: self.object.id})


class PersonDetails(ModelDetailsView):
    template_name = 'personnel/details.html'
    model = Person
    fields = ['id', 'name']
    title = 'Person\'s details'
    service = PersonService


class PersonUpdate(ModelUpdateView):
    template_name = 'personnel/update.html'
    form_class = PersonUpdateForm
    form_model = 'person'
    title = 'Update person'
    service = PersonService

    def get_success_url(self):
        return reverse('ui:person details', kwargs={ID: self.get_obj_id()})


class PersonDelete(ModelDeleteView):
    template_name = 'personnel/delete.html'
    model = Person
    form_model = 'person'
    title = 'Delete person'
    service = PersonService

    def get_success_url(self):
        return reverse('ui:person list')


class RolesAttachedToPerson(AttachedModelToModel):
    template_name = 'personnel/attached-roles.html'
    title = 'Attached roles'
    table_class = RoleTable

    def get_queryset(self):
        try:
            return PersonService.get_roles(id=self.get_obj_id())
        except:
            raise Http404("Roles does not exist")


class AttachRolesToPerson(AttachOrDetachModels):
    template_name = 'personnel/attach-roles.html'
    title = 'Attach roles'
    form_model = 'roles'
    form_class = RoleAttachForm
    obj_id_form_name = PERSON_ID

    def get_success_url(self):
        return reverse('ui:person attached roles', kwargs={ID: self.get_obj_id()})


class DetachRolesFromPerson(AttachOrDetachModels):
    template_name = 'personnel/detach-role.html'
    title = 'Detach roles'
    form_model = 'roles'
    form_class = RoleDetachForm
    obj_id_form_name = PERSON_ID

    def get_success_url(self):
        return reverse('ui:person attached roles', kwargs={ID: self.get_obj_id()})


class AttachedKeysToPerson(AttachedModelToModel):
    template_name = 'personnel/attached-keys.html'
    title = 'Attached keys'
    table_class = KeyTable

    def get_queryset(self):
        try:
            return PersonService.get_keys(id=self.get_obj_id())
        except:
            raise Http404("Person not exist")


class CreateKeyForPerson(ModelCreateView, IdToContextMixin):
    template_name = 'personnel/attach-key.html'
    title = 'Create key for person'
    form_model = 'key'
    form_class = KeyCreateForPersonForm

    def get_form_kwargs(self):
        kwargs = super(CreateKeyForPerson, self).get_form_kwargs()
        kwargs['initial'] = {
            'person_id': self.get_obj_id()
        }
        return kwargs

    def get_success_url(self):
        return reverse('ui:person attached keys', kwargs={ID: self.get_obj_id()})


class PersonAclsRules(RulesView):
    template_name = 'personnel/acl-rules.html'
    title = 'Allowed places'
    table_class = PersonACLEntryTable

    def get_queryset(self):
        return AclService.get_person_acls(person_id=self.get_obj_id())


class PersonAllowPlaces(AddRuleView):
    template_name = 'personnel/acl-allow.html'
    title = 'Allow places'
    form_class = PlaceAllowRuleForPersonForm
    form_model = 'place'
    obj_id_context_name = PERSON_ID

    def get_success_url(self):
        return reverse('ui:person acl rules', kwargs={ID: self.kwargs[ID]})


class PersonDenyPlaces(AddRuleView):
    template_name = 'personnel/acl-deny.html'
    title = 'Deny places'
    form_class = PlaceDenyRuleForPersonForm
    form_model = 'place'
    obj_id_context_name = PERSON_ID

    def get_success_url(self):
        return reverse('ui:person acl rules', kwargs={ID: self.kwargs[ID]})
