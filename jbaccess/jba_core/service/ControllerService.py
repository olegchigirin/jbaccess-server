from typing import List

from jba_core import exceptions
from jba_core.models import Controller, Door
from jba_core.service import DoorService


def get_all() -> List[Controller]:
    try:
        return list(Controller.objects.all())
    except:
        raise exceptions.SomethingWrong


def get(id: int) -> Controller:
    try:
        return Controller.objects.get(id=id)
    except Controller.DoesNotExist:
        raise exceptions.ControllerNotFound
    except:
        raise exceptions.SomethingWrong


def get_attached_doors(id: int) -> List[Door]:
    try:
        controller = Controller.objects.get(id=id)
        return list(controller.doors.all())
    except Controller.DoesNotExist:
        raise exceptions.ControllerNotFound
    except:
        raise exceptions.SomethingWrong


def create(name: str, controller_id: str) -> Controller:
    try:
        return Controller.objects.create(name=name, controller_id=controller_id)
    except:
        raise exceptions.ControllerManageFailed


def update(id: int, name: str = None, controller_id: str = None) -> Controller:
    try:
        controller = Controller.objects.get(id=id)
        if name is not None:
            controller.name = name
        if controller_id is not None:
            controller.controller_id = controller_id
        controller.save()
        return controller
    except Controller.DoesNotExist:
        raise exceptions.ControllerNotFound
    except:
        raise exceptions.ControllerManageFailed


def delete(id: int):
    try:
        Controller.objects.get(id=id).delete()
    except Controller.DoesNotExist:
        raise exceptions.ControllerNotFound
    except:
        raise exceptions.ControllerManageFailed


def attach_door(controller_id: int, door_id: int):
    try:
        controller = Controller.objects.get(id=controller_id)
    except Controller.DoesNotExist:
        raise exceptions.ControllerNotFound
    door = DoorService.get(door_id)
    if controller.doors.filter(id=door_id).count() > 0:
        raise exceptions.DoorNotFound
    try:
        controller.doors.add(door)
    except:
        raise exceptions.ControllerManageFailed


def detach_door(controller_id: int, door_id: int):
    try:
        controller = Controller.objects.get(id=controller_id)
    except Controller.DoesNotExist:
        raise exceptions.ControllerNotFound
    door = DoorService.get(door_id)
    if controller.doors.filter(id=door_id) == 0:
        raise exceptions.DoorNotFound
    try:
        controller.doors.remove(door)
    except:
        raise exceptions.ControllerManageFailed
