from typing import List

from jba_core.models import Person, Key, Role
from jba_core import exceptions


def get_all() -> List[Person]:
    try:
        return list(Person.objects.all())
    except:
        raise exceptions.SomethingWrong


def get(id: int) -> Person:
    try:
        return Person.objects.get(id=id)
    except Person.DoesNotExist:
        raise exceptions.PersonNotFound
    except:
        raise exceptions.SomethingWrong


def create(name: str) -> Person:
    try:
        return Person.objects.create(name=name)
    except:
        raise exceptions.PersonManageFailed


def update(id: int, name: str) -> Person:
    person = get(id)
    person.name = name
    try:
        person.save()
        return person
    except:
        raise exceptions.PersonManageFailed


def delete(id: int):
    person = get(id)
    try:
        person.delete()
    except:
        raise exceptions.PersonManageFailed


def get_keys(id: int) -> List[Key]:
    person = get(id)
    try:
        return list(person.key_set.all())
    except:
        raise exceptions.SomethingWrong


def get_roles(id: int) -> List[Role]:
    person = get(id)
    try:
        return list(person.roles.all())
    except:
        raise exceptions.SomethingWrong
