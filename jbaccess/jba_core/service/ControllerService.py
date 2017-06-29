from typing import Optional, List

from jba_core.models import Controller, Door


def get_all() -> Optional[List[Controller]]:
    try:
        return list(Controller.objects.all())
    except:
        return None


def get(id: int) -> Optional[Controller]:
    try:
        return Controller.objects.get(id=id)
    except:
        return None


def get_attached_doors(id: int) -> Optional[List[Door]]:
    try:
        controller = Controller.objects.get(id=id)
        return list(controller.doors.all())
    except:
        return None


def create(name: str, controller_id: str) -> Optional[Controller]:
    try:
        return Controller.objects.create(name=name, controller_id=controller_id)
    except:
        return None


def update(id: int, name: str = None, controller_id: str = None) -> Optional[Controller]:
    try:
        controller = Controller.objects.get(id=id)
        if name is not None:
            controller.name = name
        if controller_id is not None:
            controller.controller_id = controller_id
        if name is not None or controller_id is not None:
            controller.save()
        return controller
    except:
        return None


def delete(id: int) -> bool:
    try:
        Controller.objects.get(id=id).delete()
        return True
    except:
        return False


def attach_door(controller_id: int, door_id: int) -> bool:
    try:
        controller = Controller.objects.get(id=controller_id)
        if controller.doors.filter(id=door_id).count() > 0:
            return False
        door = Door.objects.get(door_id)
        controller.doors.add(door)
        return True
    except:
        return False


def detach_door(controller_id: int, door_id: int) -> bool:
    try:
        controller = Controller.objects.get(id=controller_id)
        if controller.doors.filter(id=door_id) == 0:
            return False
        door = Door.objects.get(id=door_id)
        controller.doors.remove(door)
        return True
    except:
        return False
