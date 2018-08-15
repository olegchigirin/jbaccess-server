from django import forms

from jba_core.models import Person
from jba_core.service import PersonService, RoleService
from jba_ui.common.const import ID


class PersonCreateForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput)

    class Meta:
        model = Person
        fields = ['name']

    def save(self, commit=True):
        person = PersonService.create(
            name=self.cleaned_data['name']
        )
        return person


class PersonUpdateForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(required=True, widget=forms.TextInput)

    class Meta:
        model = Person
        fields = ['name']

    def save(self, commit=True):
        person = PersonService.update(
            id=self.cleaned_data['id'],
            name=self.cleaned_data['name']
        )
        return person


class PersonAttachForm(forms.Form):
    persons = forms.ModelMultipleChoiceField(queryset=PersonService.get_none(), widget=forms.CheckboxSelectMultiple(
        attrs={'class': 'checkbox checkbox-inline'}
    ))

    def __init__(self, *args, **kwargs):
        role_id = kwargs.pop('role_id', None)
        super(PersonAttachForm, self).__init__(*args, **kwargs)

        if role_id:
            persons = RoleService.get_untouched_persons(id=role_id)
            self.fields['persons'].queryset = persons
        self.fields['persons'].empty_label = None


class PersonDetachForm(forms.Form):
    persons = forms.ModelMultipleChoiceField(queryset=PersonService.get_none(), widget=forms.CheckboxSelectMultiple(
        attrs={'class': 'checkbox checkbox-inline'}
    ))

    def __init__(self, *args, **kwargs):
        role_id = kwargs.pop('role_id', None)
        super(PersonDetachForm, self).__init__(*args, **kwargs)

        if role_id:
            persons = RoleService.get_persons(id=role_id)
            self.fields['persons'].queryset = persons
        self.fields['persons'].empty_label = None
