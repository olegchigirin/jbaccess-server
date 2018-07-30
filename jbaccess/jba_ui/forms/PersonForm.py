from django import forms

from jba_core.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['id', 'name']
