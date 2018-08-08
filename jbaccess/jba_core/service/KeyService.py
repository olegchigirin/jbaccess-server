from typing import List

from django.db.models.query import EmptyQuerySet

from jba_core.models import Key
from jba_core import exceptions
from jba_core.service import PersonService


def get_all() -> List[Key]:
    try:
        return list(Key.objects.all())
    except:
        raise exceptions.SomethingWrong


def get(id: int) -> Key:
    try:
        return Key.objects.get(id=id)
    except Key.DoesNotExist:
        raise exceptions.KeyNotFound
    except:
        raise exceptions.SomethingWrong


def create(name: str, access_key: str, person_id: int) -> Key:
    person = PersonService.get(person_id)
    try:
        return Key.objects.create(name=name, access_key=access_key, person=person)
    except:
        raise exceptions.KeyManageFailed


def update(id: int, name: str = None, access_key: str = None, person_id: int = None) -> Key:
    key = get(id)
    if name is not None:
        key.name = name
    if access_key is not None:
        key.access_key = access_key
    if person_id is not None:
        person = PersonService.get(person_id)
        key.person = person
    try:
        key.save()
        return key
    except:
        raise exceptions.KeyManageFailed


def delete(id: int):
    key = get(id)
    try:
        key.delete()
    except:
        raise exceptions.KeyManageFailed


def get_none() -> EmptyQuerySet:
    try:
        return Key.objects.none()
    except:
        raise exceptions.SomethingWrong


def get_free_keys() -> List[Key]:
    try:
        return Key.objects.filter(person=None)
    except:
        raise exceptions.SomethingWrong
