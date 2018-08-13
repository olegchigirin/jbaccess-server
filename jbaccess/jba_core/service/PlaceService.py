from typing import List

from django.db.models.query import EmptyQuerySet

from jba_core import exceptions
from jba_core.models import Place, Door
from jba_core.service import DoorService


def get_none() -> EmptyQuerySet:
    try:
        return Place.objects.none()
    except:
        raise exceptions.SomethingWrong


def get_all() -> List[Place]:
    try:
        return Place.objects.all()
    except:
        raise exceptions.PlaceNotFound


def get(id: int) -> Place:
    try:
        return Place.objects.get(id=id)
    except Place.DoesNotExist:
        raise exceptions.PlaceNotFound
    except:
        raise exceptions.SomethingWrong


def create(name: str) -> Place:
    try:
        return Place.objects.create(name=name)
    except:
        raise exceptions.PlaceManageFailed


def update(id: int, name: str) -> Place:
    place = get(id)
    place.name = name
    try:
        place.save()
        return place
    except:
        raise exceptions.PlaceManageFailed


def delete(id: int):
    place = get(id)
    try:
        place.delete()
    except:
        raise exceptions.PlaceManageFailed


def get_doors(id: int) -> List[Door]:
    place = get(id)
    try:
        return place.doors.all()
    except:
        raise exceptions.SomethingWrong


def attach_door(place_id: int, door_id: int):
    place = get(place_id)
    door = DoorService.get(door_id)
    if place.doors.filter(id=door_id).count() > 0:
        raise exceptions.PlaceManageFailed
    try:
        place.doors.add(door)
    except:
        raise exceptions.PlaceManageFailed


def detach_door(place_id: int, door_id: int):
    place = get(place_id)
    door = DoorService.get(door_id)
    if place.doors.filter(id=door_id).count() == 0:
        raise exceptions.PlaceManageFailed
    try:
        place.doors.remove(door)
    except:
        raise exceptions.PlaceManageFailed


def get_untouched_doors(id: int):
    place = get(id)
    try:
        return Door.objects.exclude(place=place)
    except:
        raise exceptions.SomethingWrong