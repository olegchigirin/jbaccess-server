from typing import List

from jba_core import exceptions
from jba_core.models import Role


def get_all() -> List[Role]:
    try:
        return list(Role.objects.all())
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
