from django import forms

from jba_core.models import Key
from jba_core.service import KeyService


class KeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = ['id', 'name', 'access_key', 'person']


class KeyAttachMultipleChoiceForm(forms.Form):
    keys = forms.ModelMultipleChoiceField(queryset=KeyService.get_none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        person_id = kwargs.pop('person_id', None)
        super(KeyAttachMultipleChoiceForm, self).__init__(*args, **kwargs)

        if person_id:
            roles = KeyService.get_free_keys(person_id=person_id)
            self.fields['keys'].queryset = roles
            self.fields['keys'].empty_label = None
