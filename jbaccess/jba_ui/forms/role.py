from django import forms

from jba_core.models import Role
from jba_core.service import RoleService, PersonService


class RoleCreateForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name']


class RoleAttachForm(forms.Form):
    roles = forms.ModelMultipleChoiceField(queryset=RoleService.get_none(), widget=forms.CheckboxSelectMultiple(attrs={
        'class': 'checkbox'
    }))

    def __init__(self, *args, **kwargs):
        person_id = kwargs.pop('person_id', None)
        super(RoleAttachForm, self).__init__(*args, **kwargs)

        if person_id:
            roles = PersonService.get_untouched_roles(id=person_id)
            self.fields['roles'].queryset = roles
        self.fields['roles'].empty_label = None


class RoleDetachForm(forms.Form):
    roles = forms.ModelMultipleChoiceField(queryset=RoleService.get_none(), widget=forms.CheckboxSelectMultiple(
        attrs={'class': 'checkbox'}
    ))

    def __init__(self, *args, **kwargs):
        person_id = kwargs.pop('person_id', None)
        super(RoleDetachForm, self).__init__(*args, **kwargs)

        if person_id:
            roles = PersonService.get_roles(id=person_id)
            self.fields['roles'].queryset = roles
        self.fields['roles'].empty_label = None
