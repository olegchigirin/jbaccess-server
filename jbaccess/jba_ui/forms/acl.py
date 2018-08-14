import datetime

from django import forms

from jba_core.service import AclService

DAYS_OF_WEEK = (
    (1, 'Su'),
    (2, 'Mo'),
    (3, 'Tu'),
    (4, 'We'),
    (5, 'Th'),
    (6, 'Fr'),
    (7, 'Sa'),
)

DAYS_OF_MONTH = ((i, i) for i in range(1, 32))
MONTHS = (
    (1, 'Jan'),
    (2, 'Feb'),
    (3, 'Mar'),
    (4, 'Apr'),
    (5, 'May'),
    (6, 'Jun'),
    (7, 'Jul'),
    (8, 'Aug'),
    (9, 'Sep'),
    (10, 'Oct'),
    (11, 'Nov'),
    (12, 'Dec')
)


class ACLForm(forms.Form):
    acl_id = forms.IntegerField(widget=forms.HiddenInput)
    from_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), help_text='ex. 12:30')
    until_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), help_text='ex. 12:30')
    days_of_week = forms.MultipleChoiceField(choices=DAYS_OF_WEEK,
                                             widget=forms.CheckboxSelectMultiple)  # TODO: ADD CUSTOM WIDGET
    days_of_month = forms.MultipleChoiceField(choices=DAYS_OF_MONTH, widget=forms.CheckboxSelectMultiple)
    months = forms.MultipleChoiceField(choices=MONTHS, widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        id = kwargs.pop('id', None)
        super(ACLForm, self).__init__(*args, **kwargs)

        if id:
            pattern = AclService.get_pattern(id=id)
            self.fields['acl_id'].initial = pattern.acl_id
            self.fields['from_time'].initial = pattern.from_time
            self.fields['until_time'].initial = pattern.until_time
            self.fields['days_of_week'].initial = self._get_initial_choices(
                data=self._map_string_to_array(pattern.days_of_week),
                choices=DAYS_OF_WEEK)  # TODO: REFACTOR INITIAL CHOICES

    @staticmethod
    def _map_string_to_array(string: str):
        return list(map(int, string[1:-1].replace(' ', '').split(',')))

    @staticmethod
    def _get_initial_choices(data: list, choices: tuple):
        result = []
        for i in data:
            result.append(choices[i])
        return result

    def update(self, pattern_id):
        from_time = self.cleaned_data['from_time']
        until_time = self.cleaned_data['until_time']
        days_of_week = self.cleaned_data['days_of_week']
        days_of_month = self.cleaned_data['days_of_month']
        months = self.cleaned_data['months']
        pattern = AclService.update_pattern(
            pattern_id=pattern_id,
            from_time=datetime.timedelta(
                hours=from_time.hour,
                minutes=from_time.minute
            ),
            until_time=datetime.timedelta(
                hours=until_time.hour,
                minutes=until_time.minute
            ),
            days_of_week=list(map(int, days_of_week)),
            days_of_month=list(map(int, days_of_month)),
            months=list(map(int, months))
        )
        return pattern

    def save(self):
        acl_id = self.cleaned_data['acl_id']
        from_time = self.cleaned_data['from_time']
        until_time = self.cleaned_data['until_time']
        days_of_week = self.cleaned_data['days_of_week']
        days_of_month = self.cleaned_data['days_of_month']
        months = self.cleaned_data['months']
        pattern = AclService.create_pattern(
            acl_id=acl_id,
            from_time=datetime.timedelta(
                hours=from_time.hour,
                minutes=from_time.minute
            ),
            until_time=datetime.timedelta(
                hours=until_time.hour,
                minutes=until_time.minute
            ),
            days_of_week=list(map(int, days_of_week)),
            days_of_month=list(map(int, days_of_month)),
            months=list(map(int, months))
        )
        return pattern
