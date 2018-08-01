from django import forms

from jba_core.models import Controller, Key, Person, Role, Door, Place


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


class AttachRoleToPersonForm(forms.Form):
    person = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.RadioSelect(),
                                    label='Choose person to attach')


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
