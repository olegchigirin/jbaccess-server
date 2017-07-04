from typing import List

from jba_core import exceptions
from jba_core.models import SimpleRecurringPattern, BaseACLEntry, PersonACLEntry, AclType, RoleACLEntry
import datetime

from jba_core.service import PersonService, PlaceService, RoleService


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


def create_pattern(acl_id: int, from_time: datetime.timedelta, until_time: datetime.timedelta, days_of_week: str,
                   days_of_month: str, months: str) -> SimpleRecurringPattern:
    acl = get_acl(acl_id)
    __validate_pattern_timings_on_create_or_update(None, from_time, until_time)
    __validate_pattern_date_pattern_on_create_or_update(None, days_of_week, days_of_month, months)
    try:
        return acl.simplerecurringpattern_set.create(from_time=from_time, until_time=until_time,
                                                     days_of_week=days_of_week, days_of_month=days_of_month,
                                                     months=months)
    except:
        raise exceptions.ACLManageFailed


def delete_acl(id: int):
    acl = get_acl(id)
    try:
        acl.delete()
    except:
        raise exceptions.ACLManageFailed


def update_pattern(pattern_id: int, from_time: datetime.timedelta = None, until_time: datetime.timedelta = None,
                   days_of_week: str = None, days_of_month: str = None, months: str = None) -> SimpleRecurringPattern:
    pattern = get_pattern(pattern_id)
    __validate_pattern_timings_on_create_or_update(pattern, from_time, until_time)
    __validate_pattern_date_pattern_on_create_or_update(pattern, days_of_week, days_of_month, months)
    if from_time is not None:
        pattern.from_time = from_time
    if until_time is not None:
        pattern.until_time = until_time
    if days_of_week is not None:
        pattern.days_of_week = days_of_week
    if days_of_month is not None:
        pattern.days_of_month = days_of_month
    if months is not None:
        pattern.months = months
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
        return list(person.personaclentry_set.all())
    except:
        raise exceptions.SomethingWrong


def get_role_acls(role_id: int) -> List[RoleACLEntry]:
    role = RoleService.get(role_id)
    try:
        return list(role.roleaclentry_set.all())
    except:
        raise exceptions.SomethingWrong


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
                                                        days_of_week: str = None, days_of_month: str = None,
                                                        months: str = None):
    if pattern is None and (days_of_week is None or days_of_month is None or months is None):
        raise exceptions.PatternDatesIncorrect
    if days_of_week is None:
        days_of_week = pattern.days_of_week
    if days_of_month is None:
        days_of_month = pattern.days_of_month
    if months is None:
        months = pattern.months
    if days_of_week != '*' and days_of_month != '*':
        raise exceptions.PatternDatesIncorrect
    if days_of_week != '*':
        dow_list = days_of_week.split(',')
        for dow in dow_list:
            if dow not in [str(d) for d in range(1, 8)]:
                raise exceptions.PatternDatesIncorrect
        if len(dow_list) != len(set(dow_list)):
            raise exceptions.PatternDatesIncorrect
    if days_of_month != '*':
        dom_list = days_of_month.split(',')
        for dom in dom_list:
            if dom not in [str(d) for d in range(1, 32)]:
                raise exceptions.PatternDatesIncorrect
        if len(dom_list) != len(set(dom_list)):
            raise exceptions.PatternDatesIncorrect
    if months != '*':
        months_list = months.split(',')
        for mon in months_list:
            if mon not in [str(m) for m in range(1, 13)]:
                raise exceptions.PatternDatesIncorrect
        if len(months_list) != len(set(months_list)):
            raise exceptions.PatternDatesIncorrect
