from django import forms
from django.db.models import QuerySet

from jba_core.models import Person
from jba_core.service import PersonService


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['id', 'name']


class PersonSingleChoiceForm(forms.Form):
    person = forms.ModelChoiceField(queryset=PersonService.get_none(), widget=forms.RadioSelect(),
                                    label='Choose person to attach')

    def __init__(self, *args, **kwargs):
        person_id = kwargs.pop('person_id', None)
        super(PersonSingleChoiceForm, self).__init__(*args, **kwargs)

        if person_id:
            persons: QuerySet = PersonService.get_all()
            attached_persons = PersonService.get_roles(id=person_id)
            self.fields['person'] = persons.difference(attached_persons)
        self.fields['person'].empty_label = None


class PersonMultipleChoiceForm(forms.Form):
    person = forms.ModelMultipleChoiceField(queryset=PersonService.get_none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        role_id = kwargs.pop('role_id')
        super(PersonMultipleChoiceForm, self).__init__(*args, **kwargs)

        if role_id:
            untouched_persons = PersonService.get_untouched_to_role(role_id=role_id)
            self.fields['person'].queryset = untouched_persons
        self.fields['person'].empty_label = None
