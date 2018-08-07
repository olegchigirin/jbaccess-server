from django import forms

from jba_core.models import Controller


class ControllerForm(forms.ModelForm):
    class Meta:
        model = Controller
        fields = ['id', 'name', 'controller_id']