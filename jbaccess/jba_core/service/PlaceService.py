from typing import List

from jba_core import exceptions
from jba_core.models import Place, Door
from jba_core.service import DoorService


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
    try:
        place = Place.objects.get(id=id)
        place.name = name
        place.save()
        return place
    except Place.DoesNotExist:
        raise exceptions.PlaceNotFound
    except:
        raise exceptions.PlaceManageFailed


def delete(id: int):
    try:
        place = Place.objects.get(id=id)
        place.delete()
    except Place.DoesNotExist:
        raise exceptions.PlaceNotFound
    except:
        raise exceptions.PlaceManageFailed


def get_doors(id: int) -> List[Door]:
    try:
        place = Place.objects.get(id=id)
        return list(place.doors.all())
    except Place.DoesNotExist:
        raise exceptions.PlaceNotFound
    except:
        raise exceptions.SomethingWrong


def attach_door(place_id: int, door_id: int):
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        raise exceptions.PlaceNotFound
    door = DoorService.get(door_id)
    if place.doors.filter(id=door_id).count() > 0:
        raise exceptions.PlaceManageFailed
    try:
        place.doors.add(door)
    except:
        raise exceptions.PlaceManageFailed


def detach_door(place_id: int, door_id: int):
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        raise exceptions.PlaceNotFound
    door = DoorService.get(door_id)
    if place.doors.filter(id=door_id).count() == 0:
        raise exceptions.PlaceManageFailed
    try:
        place.doors.remove(door)
    except:
        raise exceptions.PlaceManageFailed
