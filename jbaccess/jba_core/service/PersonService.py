from typing import List

from jba_core.models import Person, Key, Role
from jba_core import exceptions


def get_all() -> List[Person]:
    try:
        return list(Person.objects.all())
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
    try:
        person = Person.objects.get(id=id)
        person.name = name
        person.save()
        return person
    except Person.DoesNotExist:
        raise exceptions.PersonNotFound
    except:
        raise exceptions.PersonManageFailed


def delete(id: int):
    try:
        person = Person.objects.get(id=id)
        person.delete()
    except Person.DoesNotExist:
        raise exceptions.PersonNotFound
    except:
        raise exceptions.PersonManageFailed
