from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from jba_core.exceptions import AclAlreadyAdded
from jba_core.models import Person
from jba_core.service import PersonService, KeyService, AclService
from jba_ui.common.const import ID, PERSON_ID, ROLES, PLACES, NAME, ACCESS_ID
from jba_ui.common.views import ModelListView, ModelCreateView, ModelDetailsView, ModelUpdateView, ModelDeleteView, \
    AttachedModelToModel, AttachModelToModel, DetachModelFromModel, AddAllowRuleView, AllowedRulesView, AddDenyRuleView
from jba_ui.forms import PersonCreateForm, RoleAttachForm, RoleDetachForm, KeyCreateForPersonForm, PlacesForm
from jba_ui.forms.personnel import PersonUpdateForm
from jba_ui.tables import PersonTable, RoleTable, KeyTable, PersonACLEntryTable


class PersonList(ModelListView):
    template_name = 'personnel/list.html'
    model = Person
    title = 'Person list'
    table_class = PersonTable
    service = PersonService

    def get_queryset(self):
        return self.get_all()


class PersonCreate(ModelCreateView):
    template_name = 'personnel/create.html'
    form_class = PersonCreateForm
    title = 'Create person'
    person_id = None

    def get_success_url(self):
        return reverse('ui:person list')


class PersonDetails(ModelDetailsView):
    template_name = 'personnel/detail.html'
    model = Person
    fields = ['id', 'name']
    title = 'Person details'
    service = PersonService

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.kwargs[ID])


class PersonUpdate(ModelUpdateView):
    template_name = 'personnel/update.html'
    form_class = PersonUpdateForm
    title = 'Person update'
    service = PersonService

    def get_form_kwargs(self):
        kwargs = super(PersonUpdate, self).get_form_kwargs()
        kwargs['initial'] = {ID: self.kwargs[ID]}
        return kwargs

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.kwargs[ID])

    def get_success_url(self):
        return reverse('ui:person details', kwargs={ID: self.kwargs[ID]})


class PersonDelete(ModelDeleteView):
    template_name = 'personnel/delete.html'
    model = Person
    title = 'Delete person'
    service = PersonService

    def get_object(self, queryset=None):
        return self.get_obj_by_id(id=self.kwargs[ID])

    def delete(self, request, *args, **kwargs):
        self.service.delete(id=self.get_object().id)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:person list')


class RolesAttachedToPerson(AttachedModelToModel):
    template_name = 'personnel/attached-roles.html'
    title = 'Attached roles'
    table_class = RoleTable

    def get_queryset(self):
        try:
            return PersonService.get_roles(id=self.kwargs[ID])
        except:
            raise Http404("Roles does not exist")


class AttachRolesToPerson(AttachModelToModel):
    template_name = 'personnel/attach-roles.html'
    title = 'Attach roles'
    form_class = RoleAttachForm

    def get_form_kwargs(self):
        kwargs = super(AttachRolesToPerson, self).get_form_kwargs()
        kwargs[PERSON_ID] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form: RoleAttachForm):
        roles = form.cleaned_data[ROLES]
        person_id = self.kwargs[ID]
        for role in roles:
            PersonService.attach_role(person_id=person_id, role_id=role.id)
        return super(AttachRolesToPerson, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:person attached roles', kwargs={ID: self.kwargs[ID]})


class DetachRolesFromPerson(DetachModelFromModel):
    template_name = 'personnel/detach-role.html'
    title = 'Detach roles'
    form_class = RoleDetachForm

    def get_form_kwargs(self):
        kwargs = super(DetachRolesFromPerson, self).get_form_kwargs()
        kwargs[PERSON_ID] = self.kwargs[ID]
        return kwargs

    def form_valid(self, form):
        person_id = self.kwargs[ID]
        roles = form.cleaned_data[ROLES]
        for role in roles:
            PersonService.detach_role(person_id=person_id, role_id=role.id)
        return super(DetachRolesFromPerson, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:person attached roles', kwargs={ID: self.kwargs[ID]})


class AttachedKeysToPerson(AttachedModelToModel):
    template_name = 'personnel/attached-keys.html'
    title = 'Attached keys'
    table_class = KeyTable

    def get_queryset(self):
        try:
            return PersonService.get_keys(id=self.kwargs[ID])
        except:
            raise Http404("Person not exist")


class AttachKeyToPerson(ModelCreateView):
    template_name = 'personnel/attach-key.html'
    title = 'Create key for person'
    form_class = KeyCreateForPersonForm

    def form_valid(self, form: KeyCreateForPersonForm):
        KeyService.create(
            name=form.cleaned_data[NAME],
            access_key=form.cleaned_data[ACCESS_ID],
            person_id=self.kwargs[ID]
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('ui:person attached keys', kwargs={ID: self.kwargs[ID]})


class PersonAllowedPlaces(AllowedRulesView):
    template_name = 'personnel/acl-rules.html'
    title = 'Allowed places'
    table_class = PersonACLEntryTable

    def get_queryset(self):
        return AclService.get_person_acls(person_id=self.kwargs[ID])


class PersonAllowPlaces(AddAllowRuleView):
    template_name = 'personnel/acl-allow.html'
    title = 'Allow places for person'
    form_class = PlacesForm

    def form_valid(self, form):
        places = form.cleaned_data[PLACES]
        for place in places:
            try:
                AclService.person_allow_place(person_id=self.kwargs[ID], place_id=place.id)
            except AclAlreadyAdded:
                continue
        return super(PersonAllowPlaces, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:person acl rules', kwargs={ID: self.kwargs[ID]})


class PersonDenyPlaces(AddDenyRuleView):
    template_name = 'personnel/acl-deny.html'
    title = 'Deny places'
    form_class = PlacesForm

    def form_valid(self, form):
        places = form.cleaned_data[PLACES]
        for place in places:
            try:
                AclService.person_deny_place(person_id=self.kwargs[ID], place_id=place.id)
            except AclAlreadyAdded:
                continue
        return super(PersonDenyPlaces, self).form_valid(form)

    def get_success_url(self):
        return reverse('ui:person acl rules', kwargs={ID: self.kwargs[ID]})
