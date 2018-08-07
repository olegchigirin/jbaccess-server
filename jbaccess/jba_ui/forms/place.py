from django import forms

from jba_core.models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['id', 'name']