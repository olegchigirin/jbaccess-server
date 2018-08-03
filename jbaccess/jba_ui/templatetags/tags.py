from django import template
from django.urls import reverse, resolve

register = template.Library()


@register.filter(name='get_obj_attr')
def get_obj_attr(obj, attr):
    return getattr(obj, attr)


@register.simple_tag(name='get_details_url')
def get_details_url(url_name: str, id: int):
    return reverse(url_name, kwargs={'id': id})
