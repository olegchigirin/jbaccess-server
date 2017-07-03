from api_commons.dto import BaseDto
from rest_framework import serializers

from jba_core.models import Role


class RoleInDto(BaseDto):
    name = serializers.CharField(required=True, max_length=255)


class RoleOutDto(BaseDto):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=255)

    @classmethod
    def from_role(cls, role: Role):
        dto = cls()
        dto.id = role.id
        dto.name = role.name
        return dto
