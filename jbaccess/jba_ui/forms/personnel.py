from django import forms

from jba_core.models import Person
from jba_core.service import PersonService, RoleService
from jba_ui.common.const import ROLE_ID, PERSONS, NAME, ID
from jba_ui.common.widget import TextInput, CheckboxSelectMultiple


class PersonCreateForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput, help_text='Person name')

    class Meta:
        model = Person
        fields = [NAME]

    def save(self, commit=True):
        person = PersonService.create(
            name=self.cleaned_data[NAME]
        )
        return person


class PersonUpdateForm(PersonCreateForm):
    id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self, commit=True):
        person = PersonService.update(
            id=self.cleaned_data[ID],
            name=self.cleaned_data[NAME]
        )
        return person


class PersonMultipleChoiceForm(forms.Form):
    role_id = forms.IntegerField(widget=forms.HiddenInput)
    persons = forms.ModelMultipleChoiceField(queryset=PersonService.get_none(), widget=CheckboxSelectMultiple)


class PersonAttachForm(PersonMultipleChoiceForm):

    def __init__(self, *args, **kwargs):
        role_id = kwargs.pop(ROLE_ID, None)
        super(PersonAttachForm, self).__init__(*args, **kwargs)

        if role_id:
            self.fields[ROLE_ID].initial = role_id
            persons = RoleService.get_untouched_persons(id=role_id)
            self.fields[PERSONS].queryset = persons
        self.fields[PERSONS].empty_label = None

    def save(self):
        persons = self.cleaned_data[PERSONS]
        role_id = self.cleaned_data[ROLE_ID]
        for person in persons:
            PersonService.attach_role(person_id=person.id, role_id=role_id)


class PersonDetachForm(PersonMultipleChoiceForm):

    def __init__(self, *args, **kwargs):
        role_id = kwargs.pop(ROLE_ID, None)
        super(PersonDetachForm, self).__init__(*args, **kwargs)

        if role_id:
            self.fields[ROLE_ID].initial = role_id
            persons = RoleService.get_persons(id=role_id)
            self.fields[PERSONS].queryset = persons
        self.fields[PERSONS].empty_label = None

    def save(self):
        role_id = self.cleaned_data[ROLE_ID]
        persons = self.cleaned_data[PERSONS]
        for person in persons:
            PersonService.detach_role(person_id=person.id, role_id=role_id)
