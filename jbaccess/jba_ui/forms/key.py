from django import forms

from jba_core.models import Key
from jba_core.service import KeyService, PersonService


class KeyCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    access_key = forms.CharField(max_length=50)
    person = forms.ModelChoiceField(queryset=PersonService.get_all(), required=True,
                                    empty_label='Choose person')

    class Meta:
        model = Key
        fields = ['name', 'access_key', 'person']


class KeyAttachMultipleChoiceForm(forms.Form):
    keys = forms.ModelMultipleChoiceField(queryset=KeyService.get_none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(KeyAttachMultipleChoiceForm, self).__init__(*args, **kwargs)
        roles = KeyService.get_free_keys()
        self.fields['keys'].queryset = roles
        self.fields['keys'].empty_label = None


class KeyDetachMultipleChoiceForm(forms.Form):
    keys = forms.ModelMultipleChoiceField(queryset=KeyService.get_none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        person_id = kwargs.pop('person_id', None)
        super(KeyDetachMultipleChoiceForm, self).__init__(*args, **kwargs)

        if person_id:
            roles = PersonService.get_keys(id=person_id)
            self.fields['keys'].queryset = roles
        self.fields['keys'].empty_label = None
