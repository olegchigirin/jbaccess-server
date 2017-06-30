from typing import List

from jba_core.models import Door
from jba_core import exceptions


def get_all() -> List[Door]:
    try:
        return list(Door.objects.all())
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
    try:
        door = Door.objects.get(id=id)
        if name is not None:
            door.name = name
        if access_id is not None:
            door.access_id = access_id
        door.save()
        return door
    except Door.DoesNotExist:
        raise exceptions.DoorNotFound
    except:
        raise exceptions.DoorManageFailed


def delete(id: int):
    try:
        door = Door.objects.get(id=id)
        door.delete()
    except Door.DoesNotExist:
        raise exceptions.DoorNotFound
    except:
        raise exceptions.DoorManageFailed
