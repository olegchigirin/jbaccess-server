from typing import List

from django.db.models.query import EmptyQuerySet

from jba_core.models import Person, Key, Role
from jba_core import exceptions
from jba_core.service import RoleService, ControllerService


def get_none() -> EmptyQuerySet:
    try:
        return Person.objects.none()
    except:
        raise exceptions.SomethingWrong


def get_all() -> List[Person]:
    try:
        return Person.objects.all()
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
        return person.key_set.all()
    except:
        raise exceptions.SomethingWrong


def get_roles(id: int) -> List[Role]:
    person = get(id)
    try:
        return person.roles.all()
    except:
        raise exceptions.SomethingWrong


def attach_role(person_id: int, role_id: int):
    person = get(person_id)
    role = RoleService.get(role_id)
    if person.roles.filter(id=role_id).count() > 0:
        raise exceptions.RoleNotFound
    try:
        person.roles.add(role)
    except:
        raise exceptions.PersonManageFailed


def detach_role(person_id: int, role_id: int):
    person = get(person_id)
    role = RoleService.get(role_id)
    if person.roles.filter(id=role_id).count() == 0:
        raise exceptions.RoleNotFound
    try:
        person.roles.remove(role)
    except:
        raise exceptions.PersonManageFailed


def get_untouched_roles(id: int):
    person = get(id)
    try:
        return Role.objects.exclude(person=person)
    except:
        raise exceptions.SomethingWrong


def get_untouched_to_role(role_id: int):
    role = RoleService.get(role_id)
    try:
        return Person.objects.exclude(roles__in=role)
    except:
        raise exceptions.SomethingWrong
