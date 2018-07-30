from django import forms

from jba_core.models import Key


class KeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = ['id', 'name', 'access_key', 'person']