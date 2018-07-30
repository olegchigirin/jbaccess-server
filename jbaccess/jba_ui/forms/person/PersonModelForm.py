from django import forms
from jba_core.models import Person
from jba_core.service import RoleService


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['id', 'name']