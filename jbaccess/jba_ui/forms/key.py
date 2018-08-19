from django import forms
from django.http import Http404

from jba_core.models import Key
from jba_core.service import PersonService, KeyService
from jba_ui.common.widget import TextInput


class KeyCreateForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput, help_text='Key name')
    access_key = forms.CharField(widget=TextInput, help_text='Access key')
    person = forms.ModelChoiceField(queryset=PersonService.get_all(),
                                    help_text='Choose person for key',
                                    empty_label='Choose person',
                                    widget=forms.Select)

    class Meta:
        model = Key
        fields = ['name', 'access_key', 'person']

    def save(self, commit=True):
        key = KeyService.create(
            name=self.cleaned_data['name'],
            access_key=self.cleaned_data['access_key'],
            person_id=self.cleaned_data['person'].id
        )
        return key


class KeyCreateForPersonForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput, help_text='Key name')
    access_key = forms.CharField(widget=TextInput, help_text='Access key')
    person_id = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Key
        fields = ['name', 'access_key']

    def save(self, commit=True):
        key = KeyService.create(
            name=self.cleaned_data['name'],
            access_key=self.cleaned_data['access_key'],
            person_id=self.cleaned_data['person_id']
        )
        return key


class KeyUpdateForm(KeyCreateForm):
    id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self, commit=True):
        key = KeyService.update(
            id=self.cleaned_data['id'],
            name=self.cleaned_data['name'],
            access_key=self.cleaned_data['access_key'],
            person_id=self.cleaned_data['person'].id
        )
        return key
