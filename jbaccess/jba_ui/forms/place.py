from django import forms

from jba_core.models import Place
from jba_core.service import PlaceService, DoorService


class PlaceCreateForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name']


class PlaceAttachForm(forms.Form):
    places = forms.ModelMultipleChoiceField(queryset=PlaceService.get_none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        door_id = kwargs.pop('door_id', None)
        super(PlaceAttachForm, self).__init__(*args, **kwargs)

        if door_id:
            places = DoorService.get_untouched_places(id=door_id)
            self.fields['places'].queryset = places
        self.fields['places'].empty_label = None


class PlaceDetachForm(forms.Form):
    places = forms.ModelMultipleChoiceField(queryset=PlaceService.get_none(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        door_id = kwargs.pop('door_id', None)
        super(PlaceDetachForm, self).__init__(*args, **kwargs)

        if door_id:
            places = DoorService.get_attached_places(id=door_id)
            self.fields['places'].queryset = places
        self.fields['places'].empty_label = None


class PlacesForm(forms.Form):
    places = forms.ModelMultipleChoiceField(queryset=PlaceService.get_all(), widget=forms.CheckboxSelectMultiple)
