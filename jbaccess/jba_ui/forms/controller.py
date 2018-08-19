from django import forms

from jba_core.models import Controller
from jba_core.service import ControllerService, DoorService
from jba_ui.common.widget import CheckboxSelectMultiple, TextInput


class ControllerCreateForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput, help_text='controller name')
    controller_id = forms.CharField(widget=TextInput, help_text='controller id')

    class Meta:
        model = Controller
        fields = ['name', 'controller_id']

    def save(self, commit=True):
        controller = ControllerService.create(
            name=self.cleaned_data['name'],
            controller_id=self.cleaned_data['controller_id']
        )
        return controller


class ControllerUpdateForm(ControllerCreateForm):
    id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self, commit=True):
        controller = ControllerService.update(
            id=self.cleaned_data['id'],
            name=self.cleaned_data['name'],
            controller_id=self.cleaned_data['controller_id']
        )
        return controller


class ControllerMultipleChoiceForm(forms.Form):
    controllers = forms.ModelMultipleChoiceField(queryset=ControllerService.get_none(), widget=CheckboxSelectMultiple)
    door_id = forms.IntegerField(widget=forms.HiddenInput)


class ControllerAttachForm(ControllerMultipleChoiceForm):

    def __init__(self, *args, **kwargs):
        door_id = kwargs.pop('door_id', None)
        super(ControllerAttachForm, self).__init__(*args, **kwargs)

        if door_id:
            self.fields['door_id'].initial = door_id
            controllers = DoorService.get_untouched_controllers(door_id=door_id)
            self.fields['controllers'].queryset = controllers
        self.fields['controllers'].empty_label = None

    def save(self):
        controllers = self.cleaned_data['controllers']
        door_id = self.cleaned_data['door_id']
        for controller in controllers:
            ControllerService.attach_door(controller_id=controller.id, door_id=door_id)


class ControllerDetachForm(ControllerMultipleChoiceForm):

    def __init__(self, *args, **kwargs):
        door_id = kwargs.pop('door_id', None)
        super(ControllerDetachForm, self).__init__(*args, **kwargs)

        if door_id:
            self.fields['door_id'].initial = door_id
            controllers = DoorService.get_attached_controllers(id=door_id)
            self.fields['controllers'].queryset = controllers
        self.fields['controllers'].empty_label = None

    def save(self):
        controllers = self.cleaned_data['controllers']
        door_id = self.cleaned_data['door_id']
        for controller in controllers:
            ControllerService.detach_door(controller_id=controller.id, door_id=door_id)
