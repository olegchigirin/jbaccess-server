from django import forms

from jba_core.models import Door
from jba_core.service import DoorService, ControllerService, PlaceService
from jba_ui.common.const import CONTROLLER_ID, PLACE_ID, DOORS, NAME, ACCESS_ID, ID
from jba_ui.common.widget import CheckboxSelectMultiple, TextInput


class DoorCreateForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput, help_text='Door name')
    access_id = forms.CharField(widget=TextInput, help_text='Door name')

    class Meta:
        model = Door
        fields = [NAME, ACCESS_ID]

    def save(self, commit=True):
        door = DoorService.create(
            name=self.cleaned_data[NAME],
            access_id=self.cleaned_data[ACCESS_ID]
        )
        return door


class DoorUpdateForm(DoorCreateForm):
    id = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        fields = [ID, NAME, ACCESS_ID]

    def save(self, commit=True):
        door = DoorService.update(
            id=self.cleaned_data[ID],
            name=self.cleaned_data[NAME],
            access_id=self.cleaned_data[ACCESS_ID]
        )
        return door


class DoorMultipleChoiceForm(forms.Form):
    doors = forms.ModelMultipleChoiceField(queryset=DoorService.get_none(), widget=CheckboxSelectMultiple)


class DoorAttachToControllerForm(DoorMultipleChoiceForm):
    controller_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        controller_id = kwargs.pop(CONTROLLER_ID, None)
        super(DoorAttachToControllerForm, self).__init__(*args, **kwargs)

        if controller_id:
            self.fields[CONTROLLER_ID].initial = controller_id
            doors = ControllerService.get_untouched_doors(id=controller_id)
            self.fields[DOORS].queryset = doors
        self.fields[DOORS].empty_label = None

    def save(self):
        controller_id = self.cleaned_data[CONTROLLER_ID]
        doors = self.cleaned_data[DOORS]
        for door in doors:
            ControllerService.attach_door(controller_id=controller_id, door_id=door.id)


class DoorAttachToPlaceForm(DoorMultipleChoiceForm):
    place_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        place_id = kwargs.pop(PLACE_ID, None)
        super(DoorAttachToPlaceForm, self).__init__(*args, **kwargs)

        if place_id:
            self.fields[PLACE_ID].initial = place_id
            doors = PlaceService.get_untouched_doors(id=place_id)
            self.fields[DOORS].queryset = doors
        self.fields[DOORS].empty_label = None

    def save(self):
        place_id = self.cleaned_data[PLACE_ID]
        doors = self.cleaned_data[DOORS]
        for door in doors:
            PlaceService.attach_door(place_id=place_id, door_id=door.id)


class DoorDetachControllerForm(DoorMultipleChoiceForm):
    controller_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        controller_id = kwargs.pop(CONTROLLER_ID, None)
        super(DoorDetachControllerForm, self).__init__(*args, **kwargs)

        if controller_id:
            self.fields[CONTROLLER_ID] = forms.IntegerField(widget=forms.HiddenInput, initial=controller_id)
            doors = ControllerService.get_doors(id=controller_id)
            self.fields[DOORS].queryset = doors
        self.fields[DOORS].empty_label = None

    def save(self):
        if self.cleaned_data[PLACE_ID]:
            place_id = self.cleaned_data[PLACE_ID]
            doors = self.cleaned_data[DOORS]
            for door in doors:
                PlaceService.detach_door(place_id=place_id, door_id=door.id)
        if self.cleaned_data[CONTROLLER_ID]:
            controller_id = self.cleaned_data[CONTROLLER_ID]
            doors = self.cleaned_data[DOORS]
            for door in doors:
                ControllerService.detach_door(controller_id=controller_id, door_id=door.id)


class DoorDetachPlaceForm(DoorMultipleChoiceForm):
    place_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        place_id = kwargs.pop(PLACE_ID, None)
        super(DoorDetachPlaceForm, self).__init__(*args, **kwargs)

        if place_id:
            self.fields[PLACE_ID].initial = place_id
            doors = PlaceService.get_doors(id=place_id)
            self.fields[DOORS].queryset = doors
        self.fields[DOORS].empty_label = None

    def save(self):
        place_id = self.cleaned_data[PLACE_ID]
        doors = self.cleaned_data[DOORS]
        for door in doors:
            PlaceService.detach_door(place_id=place_id, door_id=door.id)
