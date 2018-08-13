from django import forms

from jba_core.models import Controller
from jba_core.service import ControllerService, DoorService


class ControllerCreateForm(forms.ModelForm):
    class Meta:
        model = Controller
        fields = ['name', 'controller_id']


class ControllerAttachForm(forms.Form):
    controllers = forms.ModelMultipleChoiceField(queryset=ControllerService.get_none(),
                                                 widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        door_id = kwargs.pop('door_id', None)
        super(ControllerAttachForm, self).__init__(*args, **kwargs)

        if door_id:
            controllers = DoorService.get_untouched_controllers(door_id=door_id)
            self.fields['controllers'].queryset = controllers
        self.fields['controllers'].empty_label = None


class ControllerDetachForm(forms.Form):
    controllers = forms.ModelMultipleChoiceField(queryset=ControllerService.get_none(),
                                                 widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        door_id = kwargs.pop('door_id', None)
        super(ControllerDetachForm, self).__init__(*args, **kwargs)

        if door_id:
            controllers = DoorService.get_attached_controllers(id=door_id)
            self.fields['controllers'].queryset = controllers
        self.fields['controllers'].empty_label = None
