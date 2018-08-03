from django import forms

from django import forms
from django.db.models import QuerySet

from jba_core.models import Controller, Key, Person, Role, Door, Place
from jba_core.service import PersonService, DoorService, RoleService, ControllerService


class ControllerForm(forms.ModelForm):
    class Meta:
        model = Controller
        fields = ['id', 'name', 'controller_id']


class DoorChoiceForm(forms.Form):
    door = forms.ModelChoiceField(queryset=DoorService.get_none(), widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        controller_id = kwargs.pop('controller_id', None)
        super(DoorChoiceForm, self).__init__(*args, **kwargs)

        if controller_id:
            doors: QuerySet = DoorService.get_all()
            attached_doors = ControllerService.get_attached_doors(id=controller_id)
            self.fields['door'].queryset = doors.difference(attached_doors)
        self.fields['door'].empty_label = None


class KeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = ['id', 'name', 'access_key', 'person']


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


class RoleMultiChoiceForm(forms.Form):
    roles = forms.ModelMultipleChoiceField(queryset=RoleService.get_none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        person_id = kwargs.pop('person_id', None)
        super(RoleMultiChoiceForm, self).__init__(*args, **kwargs)

        if person_id:
            roles = PersonService.get_roles(id=person_id)
            self.fields['roles'].queryset = roles
        self.fields['roles'].empty_label = None


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
