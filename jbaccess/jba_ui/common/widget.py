from django.forms import widgets


class NumberMultipleSelect(widgets.SelectMultiple):
    template_name = 'basic/includes/static/widget.html'

    class Media:
        css = {
            'all': ('css/multipicker.min.css',)
        }
        js = (
            'js/jquery-3.3.1.min.js',
            'js/multipicker.min.js'
        )
