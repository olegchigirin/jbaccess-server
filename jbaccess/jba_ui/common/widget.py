from django.forms import widgets


class TextInput(widgets.TextInput):
    default_attrs = {
        'class': 'form-control',
        'id': 'text-input'
    }

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        self.default_attrs.update(attrs)
        super(TextInput, self).__init__(attrs=self.default_attrs)


class CheckboxSelectMultiple(widgets.CheckboxSelectMultiple):
    template_name = 'basic/static/checkbox-select-multiple.html'
    default_attrs = {
        'group_class': 'form-check-inline form-check',
        'label_class': 'form-check-label',
        'input_class': 'form-check-input',
        'class': '',
        'type': 'checkbox',
        'min_width': '33%',
    }

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        self.default_attrs.update(attrs)
        super(CheckboxSelectMultiple, self).__init__(attrs=self.default_attrs)


class TimeInput(widgets.TimeInput):
    template_name = 'basic/static/datetime-picker.html'
    default_attrs = {
        'class': 'form-control'
    }

    def __init__(self, attrs=None, format=None):
        if attrs is None:
            attrs = {}
        self.default_attrs.update(attrs)
        super(TimeInput, self).__init__(attrs=self.default_attrs, format=format)

    class Media:
        css = {
            'all': ('css/timepicki.css',)
        }
        js = (
            'js/timepicki.js',)
