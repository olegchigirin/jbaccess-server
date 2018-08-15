from django import forms

from jba_core.models import Key
from jba_core.service import PersonService


class KeyCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    access_key = forms.CharField(max_length=50)
    person = forms.ModelChoiceField(
        queryset=PersonService.get_all(),
        required=True,
        empty_label='Choose person',
        widget=forms.Select)

    class Meta:
        model = Key
        fields = ['name', 'access_key', 'person']


class KeyCreateForPersonForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    access_key = forms.CharField(max_length=50)

    class Meta:
        model = Key
        fields = ['name', 'access_key']
