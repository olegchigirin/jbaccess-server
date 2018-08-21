import datetime
import ast

from django import forms
from django.core.exceptions import ValidationError

from jba_core.service import AclService
from jba_ui.common.const import DAYS_OF_WEEK, DAYS_OF_MONTH, MONTHS
from jba_ui.common.widget import TimeInput, CheckboxSelectMultiple


class ACLForm(forms.Form):
    from_time = forms.TimeField(widget=TimeInput(format='%H:%M'), help_text='ex. 12:30', required=True)
    until_time = forms.TimeField(widget=TimeInput(format='%H:%M'), help_text='ex. 12:30', required=True)
    days_of_week = forms.MultipleChoiceField(choices=DAYS_OF_WEEK,
                                             widget=CheckboxSelectMultiple(attrs={'min_width': '8%'}))
    days_of_month = forms.MultipleChoiceField(choices=DAYS_OF_MONTH,
                                              widget=CheckboxSelectMultiple(attrs={'min_width': '8%'}))
    months = forms.MultipleChoiceField(choices=MONTHS,
                                       widget=CheckboxSelectMultiple(attrs={'min_width': '7%'}))

    def clean(self):
        cleaned_data = super(ACLForm, self).clean()
        try:
            from_time = cleaned_data['from_time']
        except KeyError:
            return cleaned_data
        try:
            until_time = cleaned_data['until_time']
        except KeyError:
            return cleaned_data
        if until_time < from_time:
            self.add_error(field=None, error=ValidationError('Until time should be before from time'))
        return cleaned_data

    def clean_from_time(self):
        from_time = self._get_timedelta(self.cleaned_data['from_time'])
        return from_time

    def clean_until_time(self):
        until_time = self._get_timedelta(self.cleaned_data['until_time'])
        return until_time

    def clean_days_of_month(self):
        days_of_month = self.cleaned_data['days_of_month']
        return list(map(int, days_of_month))

    def clean_days_of_week(self):
        days_of_week = self.cleaned_data['days_of_week']
        return list(map(int, days_of_week))

    def clean_months(self):
        months = self.cleaned_data['months']
        return list(map(int, months))

    @staticmethod
    def _get_timedelta(time):
        return datetime.timedelta(
            hours=time.hour,
            minutes=time.minute
        )


class ACLCreateForm(ACLForm):
    acl_id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        pattern = AclService.create_pattern(
            acl_id=self.cleaned_data['acl_id'],
            from_time=self.cleaned_data['from_time'],
            until_time=self.cleaned_data['until_time'],
            days_of_week=self.cleaned_data['days_of_week'],
            days_of_month=self.cleaned_data['days_of_month'],
            months=self.cleaned_data['months'],
        )
        return pattern


class ACLUpdateForm(ACLForm):
    pattern_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        pattern_id = kwargs.pop('pattern_id', None)
        super(ACLUpdateForm, self).__init__(*args, **kwargs)

        if pattern_id:
            pattern = AclService.get_pattern(id=pattern_id)
            self.fields['pattern_id'].initial = pattern_id
            self.fields['from_time'].initial = pattern.from_time
            self.fields['until_time'].initial = pattern.until_time
            self.fields['days_of_week'].initial = ast.literal_eval(pattern.days_of_week)
            self.fields['days_of_month'].initial = ast.literal_eval(pattern.days_of_month)
            self.fields['months'].initial = ast.literal_eval(pattern.months)

    def save(self):
        pattern = AclService.update_pattern(
            pattern_id=self.cleaned_data['pattern_id'],
            from_time=self.cleaned_data['from_time'],
            until_time=self.cleaned_data['until_time'],
            days_of_week=self.cleaned_data['days_of_week'],
            days_of_month=self.cleaned_data['days_of_month'],
            months=self.cleaned_data['months']
        )
        return pattern
