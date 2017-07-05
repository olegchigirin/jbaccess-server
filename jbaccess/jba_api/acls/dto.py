from api_commons.dto import BaseDto
from rest_framework import serializers
from jba_core.models import SimpleRecurringPattern, AclType, RoleACLEntry, PersonACLEntry


class AclOutDto(BaseDto):
    id = serializers.IntegerField(required=True)
    place_id = serializers.IntegerField(required=True)
    type = serializers.ChoiceField(AclType.acl_choices, required=True)


class RoleAclOutDto(AclOutDto):
    role_id = serializers.IntegerField(required=True)

    @classmethod
    def from_role_acl(cls, acl: RoleACLEntry):
        dto = cls()
        dto.id = acl.id
        dto.place_id = acl.place.id
        dto.role_id = acl.role.id
        dto.type = acl.type
        return dto


class PersonAclOutDto(AclOutDto):
    person_id = serializers.IntegerField(required=True)

    @classmethod
    def from_person_acl(cls, acl: PersonACLEntry):
        dto = cls()
        dto.id = acl.id
        dto.place_id = acl.place.id
        dto.person_id = acl.person.id
        dto.type = acl.type
        return dto


class SimplePatternInDto(BaseDto):
    from_time = serializers.DurationField(required=True)
    until_time = serializers.DurationField(required=True)
    days_of_week = serializers.ListField(required=True)
    days_of_month = serializers.ListField(required=True)
    months = serializers.ListField(required=True)


class SimplePatternOutDto(BaseDto):
    id = serializers.IntegerField(required=True)
    acl_id = serializers.IntegerField(required=True)
    from_time = serializers.DurationField(required=True)
    until_time = serializers.DurationField(required=True)
    days_of_week = serializers.ListField(required=True)
    days_of_month = serializers.ListField(required=True)
    months = serializers.ListField(required=True)

    @classmethod
    def from_simple_pattern(cls, pattern: SimpleRecurringPattern):
        dto = cls()
        dto.id = pattern.id
        dto.acl_id = pattern.acl.id
        dto.from_time = pattern.from_time
        dto.until_time = pattern.until_time
        dto.days_of_week = pattern.get_days_of_week()
        dto.days_of_month = pattern.get_days_of_month()
        dto.months = pattern.get_months()
        return dto
