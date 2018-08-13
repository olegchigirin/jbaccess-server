from typing import List

from django.db.models.query import EmptyQuerySet

from jba_core.models import Door, Controller, Place
from jba_core import exceptions


def get_none() -> EmptyQuerySet:
    try:
        return Door.objects.none()
    except:
        raise exceptions.SomethingWrong


def get_all() -> List[Door]:
    try:
        return Door.objects.all()
    except:
        raise exceptions.SomethingWrong


def get(id: int) -> Door:
    try:
        return Door.objects.get(id=id)
    except Door.DoesNotExist:
        raise exceptions.DoorNotFound
    except:
        raise exceptions.SomethingWrong


def create(name: str, access_id: str) -> Door:
    try:
        return Door.objects.create(name=name, access_id=access_id)
    except:
        raise exceptions.DoorManageFailed


def update(id: int, name: str = None, access_id: str = None) -> Door:
    door = get(id)
    if name is not None:
        door.name = name
    if access_id is not None:
        door.access_id = access_id
    try:
        door.save()
        return door
    except:
        raise exceptions.DoorManageFailed


def delete(id: int):
    door = get(id)
    try:
        door.delete()
    except:
        raise exceptions.DoorManageFailed


def get_untouched_controllers(door_id: int) -> List[Controller]:
    door = get(door_id)
    try:
        return Controller.objects.exclude(doors=door)
    except:
        raise exceptions.SomethingWrong


def get_attached_controllers(id: int) -> List[Controller]:
    door = get(id)
    try:
        return door.controller_set.all()
    except:
        raise exceptions.SomethingWrong


def get_attached_places(id: int):
    door = get(id)
    try:
        return door.place_set.all()
    except:
        raise exceptions.SomethingWrong


def get_untouched_places(id: int) -> List[Place]:
    door = get(id)
    try:
        return Place.objects.exclude(doors=door)
    except:
        raise exceptions.SomethingWrong