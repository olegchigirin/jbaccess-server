from api_commons.dto import BaseDto
from rest_framework import serializers

from jba_core.models import Person


class PersonOutDto(BaseDto):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=255)

    @classmethod
    def from_person(cls, person: Person):
        dto = cls()
        dto.id = person.id
        dto.name = person.name
        return dto


class PersonInDto(BaseDto):
    name = serializers.CharField(required=True, max_length=255)
