from django import forms

from jba_core.models import Role
from jba_core.service import RoleService, PersonService
from jba_ui.common.widget import CheckboxSelectMultiple, TextInput


class RoleCreateForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput, help_text='Role name')

    class Meta:
        model = Role
        fields = ['name']

    def save(self, commit=True):
        role = RoleService.create(name=self.cleaned_data['name'])
        return role


class RoleUpdateForm(RoleCreateForm):
    id = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        fields = ['name', 'id']

    def save(self, commit=True):
        role = RoleService.update(
            id=self.cleaned_data['id'],
            name=self.cleaned_data['name']
        )
        return role


class RoleAttachForm(forms.Form):
    person_id = forms.IntegerField(widget=forms.HiddenInput)
    roles = forms.ModelMultipleChoiceField(queryset=RoleService.get_none(), widget=CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        person_id = kwargs.pop('person_id', None)
        super(RoleAttachForm, self).__init__(*args, **kwargs)

        if person_id:
            self.fields['person_id'].initial = person_id
            roles = PersonService.get_untouched_roles(id=person_id)
            self.fields['roles'].queryset = roles
        self.fields['roles'].empty_label = None

    def save(self):
        roles = self.cleaned_data['roles']
        person_id = self.cleaned_data['person_id']
        for role in roles:
            PersonService.attach_role(person_id=person_id, role_id=role.id)


class RoleDetachForm(forms.Form):
    person_id = forms.IntegerField(widget=forms.HiddenInput)
    roles = forms.ModelMultipleChoiceField(queryset=RoleService.get_none(), widget=CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        person_id = kwargs.pop('person_id', None)
        super(RoleDetachForm, self).__init__(*args, **kwargs)

        if person_id:
            self.fields['person_id'].initial = person_id
            roles = PersonService.get_roles(id=person_id)
            self.fields['roles'].queryset = roles
        self.fields['roles'].empty_label = None

    def save(self):
        person_id = self.cleaned_data['person_id']
        roles = self.cleaned_data['roles']
        for role in roles:
            PersonService.detach_role(person_id=person_id, role_id=role.id)
