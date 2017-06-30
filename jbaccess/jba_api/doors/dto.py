from api_commons.dto import BaseDto
from rest_framework import serializers

from jba_core.models import Door


class DoorInDto(BaseDto):
    name = serializers.CharField(required=True, max_length=255)
    access_id = serializers.CharField(required=True, max_length=255)


class DoorOutDto(BaseDto):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=255)
    access_id = serializers.CharField(required=True, max_length=255)

    @classmethod
    def from_door(cls, door: Door):
        dto = cls()
        dto.id = door.id
        dto.name = door.name
        dto.access_id = door.access_id
