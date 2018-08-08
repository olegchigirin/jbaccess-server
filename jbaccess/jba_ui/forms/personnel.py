from django import forms

from jba_core.models import Person
from jba_core.service import PersonService, RoleService


class PersonForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=50, min_length=20, widget=forms.TextInput)

    class Meta:
        model = Person
        fields = ['id', 'name']


class AttachPersonsMultipleChoiceForm(forms.Form):
    persons = forms.ModelMultipleChoiceField(queryset=PersonService.get_none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        role_id = kwargs.pop('role_id', None)
        super(AttachPersonsMultipleChoiceForm, self).__init__(*args, **kwargs)

        if role_id:
            persons = RoleService.get_untouched_persons(id=role_id)
            self.fields['persons'].queryset = persons
        self.fields['persons'].empty_label = None


class DetachPersonMultipleChoiceForm(forms.Form):
    persons = forms.ModelMultipleChoiceField(queryset=PersonService.get_none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        role_id = kwargs.pop('role_id', None)
        super(DetachPersonMultipleChoiceForm, self).__init__(*args, **kwargs)

        if role_id:
            persons = RoleService.get_persons(id=role_id)
            self.fields['persons'].queryset = persons
        self.fields['persons'].empty_label = None
