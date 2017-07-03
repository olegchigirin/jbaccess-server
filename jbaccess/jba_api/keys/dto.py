from api_commons.dto import BaseDto
from rest_framework import serializers

from jba_core.models import Key


class KeyInDto(BaseDto):
    name = serializers.CharField(required=True, max_length=255)
    access_key = serializers.CharField(required=True, max_length=255)
    person_id = serializers.IntegerField(required=True)


class KeyOutDto(BaseDto):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=255)
    access_key = serializers.CharField(required=True, max_length=255)
    person_id = serializers.IntegerField(required=True)

    @classmethod
    def from_key(cls, key: Key):
        dto = cls()
        dto.id = key.id
        dto.name = key.name
        dto.access_key = key.access_key
        dto.person_id = key.person.id
        return dto
