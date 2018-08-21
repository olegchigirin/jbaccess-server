from typing import List

from django.db.models.query import EmptyQuerySet, QuerySet

from jba_core import exceptions
from jba_core.models import Controller, Door
from jba_core.service import DoorService


def get_none() -> EmptyQuerySet:
    try:
        return Controller.objects.none()
    except:
        raise exceptions.SomethingWrong


def get_all() -> QuerySet:
    try:
        return Controller.objects.all()
    except:
        raise exceptions.SomethingWrong


def get(id: int) -> Controller:
    try:
        return Controller.objects.get(id=id)
    except Controller.DoesNotExist:
        raise exceptions.ControllerNotFound
    except:
        raise exceptions.SomethingWrong


def get_by_controller_id(controller_id: str) -> Controller:
    try:
        return Controller.objects.get(controller_id__iexact=controller_id)
    except Controller.DoesNotExist:
        raise exceptions.ControllerNotFound
    except:
        raise exceptions.SomethingWrong


def get_doors(id: int) -> List[Door]:
    controller = get(id)
    try:
        return controller.doors.all()
    except:
        raise exceptions.SomethingWrong


def create(name: str, controller_id: str) -> Controller:
    try:
        return Controller.objects.create(name=name, controller_id=controller_id)
    except:
        raise exceptions.ControllerManageFailed


def update(id: int, name: str = None, controller_id: str = None) -> Controller:
    controller = get(id)
    if name is not None:
        controller.name = name
    if controller_id is not None:
        controller.controller_id = controller_id
    try:
        controller.save()
        return controller
    except:
        raise exceptions.ControllerManageFailed


def delete(id: int):
    controller = get(id)
    try:
        controller.delete()
    except:
        raise exceptions.ControllerManageFailed


def attach_door(controller_id: int, door_id: int):
    controller = get(controller_id)
    door = DoorService.get(door_id)
    if controller.doors.filter(id=door_id).count() > 0:
        raise exceptions.DoorNotFound
    try:
        controller.doors.add(door)
    except:
        raise exceptions.ControllerManageFailed


def detach_door(controller_id: int, door_id: int):
    controller = get(controller_id)
    door = DoorService.get(door_id)
    if controller.doors.filter(id=door_id) == 0:
        raise exceptions.DoorNotFound
    try:
        controller.doors.remove(door)
    except:
        raise exceptions.ControllerManageFailed


def get_untouched_doors(id: int) -> List[Door]:
    controller = get(id)
    try:
        return Door.objects.exclude(controller=controller)
    except:
        raise exceptions.SomethingWrong
