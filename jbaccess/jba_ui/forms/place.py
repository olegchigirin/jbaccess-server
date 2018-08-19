from django import forms

from jba_core.exceptions import AclAlreadyAdded
from jba_core.models import Place
from jba_core.service import PlaceService, DoorService, AclService
from jba_ui.common.const import PLACES, PERSON_ID, ROLE_ID, NAME, ID
from jba_ui.common.widget import CheckboxSelectMultiple, TextInput


class PlaceForm(forms.ModelForm):
    name = forms.CharField(widget=TextInput, help_text='Place name')

    class Meta:
        model = Place
        fields = ['name']


class PlaceCreateForm(PlaceForm):

    def save(self, commit=True):
        place = PlaceService.create(
            name=self.cleaned_data[NAME]
        )
        return place


class PlaceUpdateForm(PlaceForm):
    id = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        fields = ['id', 'name']

    def save(self, commit=True):
        place = PlaceService.update(
            id=self.cleaned_data[ID],
            name=self.cleaned_data[NAME]
        )
        return place


class PlaceMultipleChoiceForm(forms.Form):
    door_id = forms.IntegerField(widget=forms.HiddenInput)
    places = forms.ModelMultipleChoiceField(queryset=PlaceService.get_none(), widget=CheckboxSelectMultiple)


class PlaceAttachForm(PlaceMultipleChoiceForm):

    def __init__(self, *args, **kwargs):
        door_id = kwargs.pop('door_id', None)
        super(PlaceAttachForm, self).__init__(*args, **kwargs)

        if door_id:
            self.fields['door_id'].initial = door_id
            places = DoorService.get_untouched_places(id=door_id)
            self.fields['places'].queryset = places
        self.fields['places'].empty_label = None

    def save(self):
        places = self.cleaned_data['places']
        door_id = self.cleaned_data['door_id']
        for place in places:
            PlaceService.attach_door(place_id=place.id, door_id=door_id)


class PlaceDetachForm(forms.Form):

    def __init__(self, *args, **kwargs):
        door_id = kwargs.pop('door_id', None)
        super(PlaceDetachForm, self).__init__(*args, **kwargs)

        if door_id:
            self.fields['door_id'].initial = door_id
            places = DoorService.get_attached_places(id=door_id)
            self.fields['places'].queryset = places
        self.fields['places'].empty_label = None

    def save(self):
        places = self.cleaned_data['places']
        door_id = self.cleaned_data['door_id']
        for place in places:
            PlaceService.detach_door(place_id=place.id, door_id=door_id)


class PlaceRuleForm(forms.Form):
    places = forms.ModelMultipleChoiceField(queryset=PlaceService.get_all(), widget=CheckboxSelectMultiple)


class PlaceAllowRuleForPersonForm(PlaceRuleForm):
    person_id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        person_id = self.cleaned_data[PERSON_ID]
        places = self.cleaned_data[PLACES]
        for place in places:
            try:
                AclService.person_allow_place(person_id=person_id, place_id=place.id)
            except AclAlreadyAdded:
                continue


class PlaceDenyRuleForPersonForm(PlaceRuleForm):
    person_id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        person_id = self.cleaned_data[PERSON_ID]
        places = self.cleaned_data[PLACES]
        for place in places:
            try:
                AclService.person_deny_place(person_id=person_id, place_id=place.id)
            except AclAlreadyAdded:
                continue


class PlaceAllowRuleForRoleForm(PlaceRuleForm):
    role_id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        role_id = self.cleaned_data[ROLE_ID]
        places = self.cleaned_data[PLACES]
        for place in places:
            try:
                AclService.role_allow_place(role_id=role_id, place_id=place.id)
            except AclAlreadyAdded:
                continue


class PlaceDenyRuleForRoleForm(PlaceRuleForm):
    role_id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        role_id = self.cleaned_data[ROLE_ID]
        places = self.cleaned_data[PLACES]
        for place in places:
            try:
                AclService.role_deny_place(role_id=role_id, place_id=place.id)
            except AclAlreadyAdded:
                continue
