from django import forms
from django.db.models import QuerySet

from jba_core.models import Door
from jba_core.service import DoorService, ControllerService


class DoorChoiceForm(forms.Form):
    door = forms.ModelChoiceField(queryset=DoorService.get_none(), widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        controller_id = kwargs.pop('controller_id', None)
        super(DoorChoiceForm, self).__init__(*args, **kwargs)

        if controller_id:
            doors: QuerySet = DoorService.get_all()
            attached_doors = ControllerService.get_attached_doors(id=controller_id)
            self.fields['door'].queryset = doors.difference(attached_doors)
        self.fields['door'].empty_label = None


class DoorForm(forms.ModelForm):
    class Meta:
        model = Door
        fields = ['id', 'name', 'access_id']