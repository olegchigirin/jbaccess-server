from django import template
from django.urls import reverse

register = template.Library()


@register.filter(name='get_obj_attr')
def get_obj_attr(obj, attr):
    return getattr(obj, attr)


@register.filter()
def to_row_data(data: str):
    return data.capitalize().replace('_', ' ')


