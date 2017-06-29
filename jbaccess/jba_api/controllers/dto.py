from api_commons.dto import BaseDto
from rest_framework import serializers

from jba_core.models import Controller


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
