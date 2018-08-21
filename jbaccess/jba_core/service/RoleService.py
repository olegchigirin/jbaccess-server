from typing import List

from django.db.models.query import EmptyQuerySet, QuerySet

from jba_core import exceptions
from jba_core.models import Role, Person


def get_none() -> EmptyQuerySet:
    try:
        return Role.objects.none()
    except:
        raise exceptions.SomethingWrong


def get_all() -> QuerySet:
    try:
        return Role.objects.all()
    except:
        raise exceptions.SomethingWrong


def get(id: int) -> Role:
    try:
        return Role.objects.get(id=id)
    except Role.DoesNotExist:
        raise exceptions.RoleNotFound
    except:
        raise exceptions.SomethingWrong


def create(name: str) -> Role:
    try:
        return Role.objects.create(name=name)
    except:
        raise exceptions.RoleManageFailed


def update(id: int, name: str) -> Role:
    role = get(id)
    role.name = name
    try:
        role.save()
        return role
    except:
        raise exceptions.RoleManageFailed


def delete(id: int):
    role = get(id)
    try:
        role.delete()
    except:
        raise exceptions.RoleManageFailed


def get_untouched_persons(id: int) -> List[Person]:
    role = get(id)
    try:
        return Person.objects.exclude(roles=role)
    except:
        raise exceptions.SomethingWrong


def get_persons(id: int) -> List[Person]:
    role = get(id)
    try:
        return Person.objects.filter(roles=role)
    except:
        raise exceptions.SomethingWrong
