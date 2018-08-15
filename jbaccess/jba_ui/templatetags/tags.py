from django import template
from django.urls import reverse

register = template.Library()


@register.filter(name='get_obj_attr')
def get_obj_attr(obj, attr):
    return getattr(obj, attr)


@register.filter()
def to_row_data(data: str):
    return data.capitalize().replace('_', ' ')


@register.simple_tag(name='get_url')
def get_url(url_name: str, id: int = None):
    if id:
        return reverse(url_name, kwargs={'id': id})
    else:
        reverse(url_name)
