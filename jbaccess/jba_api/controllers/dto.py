from api_commons.dto import BaseDto
from rest_framework import serializers

from jba_core.models import Controller, AclType, Key, Door, SimpleRecurringPattern


class ControllerInDto(BaseDto):
    name = serializers.CharField(required=True, max_length=255)
    controller_id = serializers.CharField(required=True, max_length=255)


class ControllerOutDto(BaseDto):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=255)
    controller_id = serializers.CharField(required=True, max_length=255)

    @classmethod
    def from_controller(cls, controller: Controller):
        dto = cls()
        dto.id = controller.id
        dto.name = controller.name
        dto.controller_id = controller.controller_id
        return dto


class ResolvedPatternOutDto(BaseDto):
    from_time = serializers.DurationField(required=True)
    until_time = serializers.DurationField(required=True)
    days_of_week = serializers.CharField(required=True, max_length=255)
    days_of_month = serializers.CharField(required=True, max_length=255)
    months = serializers.CharField(required=True, max_length=255)

    @classmethod
    def from_pattern(cls, pattern: SimpleRecurringPattern):
        dto = cls()
        dto.from_time = pattern.from_time
        dto.until_time = pattern.until_time
        dto.days_of_week = pattern.days_of_week
        dto.days_of_month = pattern.days_of_month
        dto.months = pattern.months
        return dto


class ResolvedAclOutDto(BaseDto):
    key = serializers.CharField(required=True, max_length=255)
    door = serializers.CharField(required=True, max_length=255)
    type = serializers.ChoiceField(AclType.acl_choices, required=True)
    date_time_pattern = ResolvedPatternOutDto(required=True)

    @classmethod
    def from_values(cls, acl_type: AclType, key: Key, door: Door, pattern: SimpleRecurringPattern):
        dto = cls()
        dto.type = acl_type
        dto.key = key.access_key
        dto.door = door.access_id
        dto.date_time_pattern = ResolvedPatternOutDto.from_pattern(pattern)
        return dto
