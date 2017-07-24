from api_commons.dto import BaseDto
from rest_framework import serializers

from jba_core.models import Place


class PlaceInDto(BaseDto):
    name = serializers.CharField(required=True, max_length=255)


class PlaceOutDto(BaseDto):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=255)

    @classmethod
    def from_place(cls, place: Place):
        dto = cls()
        dto.id = place.id
        dto.name = place.name
        return dto
