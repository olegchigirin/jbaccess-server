from django import forms

from django import forms

from jba_core.models import Controller, Key, Person, Role, Door, Place
from jba_core.service import PersonService


class ControllerForm(forms.ModelForm):
    class Meta:
        model = Controller
        fields = ['id', 'name', 'controller_id']


class KeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = ['id', 'name', 'access_key', 'person']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['id', 'name']


class PersonSingleChoiceForm(forms.Form):
    person = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.RadioSelect(),
                                    label='Choose person to attach')


class RoleMultiChoiceForm(forms.Form):
    roles = forms.ModelMultipleChoiceField(queryset=Role.objects.none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        person_id = kwargs.pop('person_id', None)
        super(RoleMultiChoiceForm, self).__init__(*args, **kwargs)

        if person_id:
            roles = PersonService.get_roles(id=person_id)
            self.fields['roles'].queryset = roles


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['id', 'name']


class DoorForm(forms.ModelForm):
    class Meta:
        model = Door
        fields = ['id', 'name', 'access_id']


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['id', 'name']
