from django import forms
from django.db.models import QuerySet

from jba_core.models import Door
from jba_core.service import DoorService, ControllerService, PlaceService


class DoorCreateForm(forms.ModelForm):
    class Meta:
        model = Door
        fields = ['name', 'access_id']


class DoorAttachForm(forms.Form):
    doors = forms.ModelMultipleChoiceField(queryset=DoorService.get_none(), widget=forms.CheckboxSelectMultiple(
        attrs={'class': 'checkbox'}
    ))

    def __init__(self, *args, **kwargs):
        controller_id = kwargs.pop('controller_id', None)
        place_id = kwargs.pop('place_id', None)
        super(DoorAttachForm, self).__init__(*args, **kwargs)

        if controller_id:
            doors = ControllerService.get_untouched_doors(id=controller_id)
            self.fields['doors'].queryset = doors
        elif place_id:
            doors = PlaceService.get_untouched_doors(id=place_id)
            self.fields['doors'].queryset = doors
        self.fields['doors'].empty_label = None


class DoorDetachForm(forms.Form):
    doors = forms.ModelMultipleChoiceField(queryset=DoorService.get_none(), widget=forms.CheckboxSelectMultiple(
        attrs={'class': 'checkbox'}
    ))

    def __init__(self, *args, **kwargs):
        controller_id = kwargs.pop('controller_id', None)
        place_id = kwargs.pop('place_id', None)
        super(DoorDetachForm, self).__init__(*args, **kwargs)

        if controller_id:
            doors = ControllerService.get_doors(id=controller_id)
            self.fields['doors'].queryset = doors
        elif place_id:
            doors = PlaceService.get_doors(id=place_id)
            self.fields['doors'].queryset = doors
        self.fields['doors'].empty_label = None


class DoorChoiceForm(forms.Form):
    door = forms.ModelChoiceField(queryset=DoorService.get_none(), widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        controller_id = kwargs.pop('controller_id', None)
        super(DoorChoiceForm, self).__init__(*args, **kwargs)

        if controller_id:
            doors: QuerySet = DoorService.get_all()
            attached_doors = ControllerService.get_doors(id=controller_id)
            self.fields['door'].queryset = doors.difference(attached_doors)
        self.fields['door'].empty_label = None
