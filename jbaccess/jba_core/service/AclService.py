from typing import List, Tuple
import json
from jba_core import exceptions
from jba_core.models import SimpleRecurringPattern, BaseACLEntry, PersonACLEntry, AclType, RoleACLEntry, Door, Key
import datetime

from jba_core.service import PersonService, PlaceService, RoleService, ControllerService


def get_acl(id: int) -> BaseACLEntry:
    try:
        return BaseACLEntry.objects.get(id=id)
    except BaseACLEntry.DoesNotExist:
        raise exceptions.ACLNotFound
    except:
        raise exceptions.SomethingWrong


def get_pattern(id: int) -> SimpleRecurringPattern:
    try:
        return SimpleRecurringPattern.objects.get(id=id)
    except SimpleRecurringPattern.DoesNotExist:
        raise exceptions.PatternNotFound
    except:
        raise exceptions.SomethingWrong


def get_patterns(acl_id: int) -> List[SimpleRecurringPattern]:
    acl = get_acl(acl_id)
    try:
        return list(acl.simplerecurringpattern_set.all())
    except:
        raise exceptions.SomethingWrong


def create_pattern(acl_id: int, from_time: datetime.timedelta, until_time: datetime.timedelta, days_of_week: List[int],
                   days_of_month: List[int], months: List[int]) -> SimpleRecurringPattern:
    acl = get_acl(acl_id)
    __validate_pattern_timings_on_create_or_update(None, from_time, until_time)
    __validate_pattern_date_pattern_on_create_or_update(None, days_of_week, days_of_month, months)
    try:
        return acl.simplerecurringpattern_set.create(from_time=from_time, until_time=until_time,
                                                     days_of_week=json.dumps(days_of_week),
                                                     days_of_month=json.dumps(days_of_month), months=json.dumps(months))
    except:
        raise exceptions.ACLManageFailed


def delete_acl(id: int):
    acl = get_acl(id)
    try:
        acl.delete()
    except:
        raise exceptions.ACLManageFailed


def update_pattern(pattern_id: int, from_time: datetime.timedelta = None, until_time: datetime.timedelta = None,
                   days_of_week: List[int] = None, days_of_month: List[int] = None,
                   months: List[int] = None) -> SimpleRecurringPattern:
    pattern = get_pattern(pattern_id)
    __validate_pattern_timings_on_create_or_update(pattern, from_time, until_time)
    __validate_pattern_date_pattern_on_create_or_update(pattern, days_of_week, days_of_month, months)
    if from_time is not None:
        pattern.from_time = from_time
    if until_time is not None:
        pattern.until_time = until_time
    if days_of_week is not None:
        pattern.set_days_of_week(days_of_week)
    if days_of_month is not None:
        pattern.set_days_of_month(days_of_month)
    if months is not None:
        pattern.set_months(months)
    try:
        pattern.save()
        return pattern
    except:
        raise exceptions.PatternManageFailed


def delete_pattern(pattern_id: int):
    pattern = get_pattern(pattern_id)
    try:
        pattern.delete()
    except:
        raise exceptions.PatternManageFailed


def person_allow_place(person_id: int, place_id: int) -> PersonACLEntry:
    person = PersonService.get(person_id)
    place = PlaceService.get(place_id)
    if PersonACLEntry.objects.filter(person=person, place=place, type=AclType.ACL_ALLOW).count() > 0:
        raise exceptions.AclAlreadyAdded
    try:
        return PersonACLEntry.objects.create(person=person, place=place, type=AclType.ACL_ALLOW)
    except:
        raise exceptions.ACLManageFailed


def person_deny_place(person_id: int, place_id: int) -> PersonACLEntry:
    person = PersonService.get(person_id)
    place = PlaceService.get(place_id)
    if PersonACLEntry.objects.filter(person=person, place=place, type=AclType.ACL_DENY).count() > 0:
        raise exceptions.AclAlreadyAdded
    try:
        return PersonACLEntry.objects.create(person=person, place=place, type=AclType.ACL_DENY)
    except:
        raise exceptions.ACLManageFailed


def role_allow_place(role_id: int, place_id: int) -> RoleACLEntry:
    role = RoleService.get(role_id)
    place = PlaceService.get(place_id)
    if RoleACLEntry.objects.filter(role=role, place=place, type=AclType.ACL_ALLOW).count() > 0:
        raise exceptions.AclAlreadyAdded
    try:
        return RoleACLEntry.objects.create(role=role, place=place, type=AclType.ACL_ALLOW)
    except:
        raise exceptions.ACLManageFailed


def role_deny_place(role_id: int, place_id: int) -> RoleACLEntry:
    role = RoleService.get(role_id)
    place = PlaceService.get(place_id)
    if RoleACLEntry.objects.filter(role=role, place=place, type=AclType.ACL_DENY).count() > 0:
        raise exceptions.AclAlreadyAdded
    try:
        return RoleACLEntry.objects.create(role=role, place=place, type=AclType.ACL_DENY)
    except:
        raise exceptions.ACLManageFailed


def get_person_acls(person_id: int) -> List[PersonACLEntry]:
    person = PersonService.get(person_id)
    try:
        return person.personaclentry_set.all()
    except:
        raise exceptions.SomethingWrong


def get_role_acls(role_id: int) -> List[RoleACLEntry]:
    role = RoleService.get(role_id)
    try:
        return list(role.roleaclentry_set.all())
    except:
        raise exceptions.SomethingWrong


def resolve_acls_by_controller(controller_id: str) -> List[Tuple[AclType, Key, Door, SimpleRecurringPattern]]:
    controller = ControllerService.get_by_controller_id(controller_id)
    role_acls = list(RoleACLEntry.objects.filter(place__doors__controller=controller))
    person_acls = list(PersonACLEntry.objects.filter(place__doors__controller=controller))
    result = list()
    for acl in role_acls:
        doors = list(acl.place.doors.filter(controller=controller))
        patterns = list(acl.simplerecurringpattern_set.all())
        for person in acl.role.person_set.all():
            for key in person.key_set.all():
                for door in doors:
                    for pattern in patterns:
                        result.append((acl.type, key, door, pattern))
    for acl in person_acls:
        doors = list(acl.place.doors.filter(controller=controller))
        patterns = list(acl.simplerecurringpattern_set.all())
        for key in acl.person.key_set.all():
            for door in doors:
                for pattern in patterns:
                    result.append((acl.type, key, door, pattern))
    return result


def __validate_pattern_timings_on_create_or_update(pattern: SimpleRecurringPattern = None,
                                                   from_time: datetime.timedelta = None,
                                                   until_time: datetime.timedelta = None):
    if pattern is None and (from_time is None or until_time is None):
        raise exceptions.PatternTimingIncorrect
    if from_time is None:
        from_time = pattern.from_time
    if until_time is None:
        until_time = pattern.until_time
    __validate_pattern_timings(from_time, until_time)


def __validate_pattern_timings(from_time: datetime.timedelta, until_time: datetime.timedelta):
    elapsed = until_time - from_time
    if elapsed.total_seconds() < 0:
        raise exceptions.PatternTimingIncorrect


def __validate_pattern_date_pattern_on_create_or_update(pattern: SimpleRecurringPattern = None,
                                                        days_of_week: List[int] = None, days_of_month: List[int] = None,
                                                        months: List[int] = None):
    if pattern is None and (days_of_week is None or days_of_month is None or months is None):
        raise exceptions.PatternDatesIncorrect
    if days_of_week is None:
        days_of_week = pattern.get_days_of_week()
    if days_of_month is None:
        days_of_month = pattern.get_days_of_month()
    if months is None:
        months = pattern.get_months()
    if len(days_of_week) > 0:
        for dow in days_of_week:
            if dow not in range(1, 8):
                raise exceptions.PatternDatesIncorrect
        if len(days_of_week) != len(set(days_of_week)):
            raise exceptions.PatternDatesIncorrect
    if len(days_of_month) > 0:
        for dom in days_of_month:
            if dom not in range(1, 32):
                raise exceptions.PatternDatesIncorrect
        if len(days_of_month) != len(set(days_of_month)):
            raise exceptions.PatternDatesIncorrect
    if len(months) > 0:
        for mon in months:
            if mon not in range(1, 13):
                raise exceptions.PatternDatesIncorrect
        if len(months) != len(set(months)):
            raise exceptions.PatternDatesIncorrect
