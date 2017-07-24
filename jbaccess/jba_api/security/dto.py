from api_commons.dto import BaseDto
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class LoginInDto(BaseDto):
    login = serializers.CharField(required=True, min_length=1, max_length=255)
    password = serializers.CharField(required=True, min_length=1, max_length=255)


class UserGroupOutDto(BaseDto):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, min_length=1, max_length=255)

    @classmethod
    def from_group(cls, group: Group):
        dto = cls()
        dto.id = group.id
        dto.name = group.name
        return dto


class UserInfoOutDto(BaseDto):
    id = serializers.IntegerField(required=True)
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)
    is_superuser = serializers.BooleanField(required=True)
    groups = serializers.ListField(required=True)

    @classmethod
    def from_user(cls, user: User):
        dto = cls()
        dto.id = user.id
        dto.username = user.username
        dto.first_name = user.first_name
        dto.last_name = user.last_name
        dto.email = user.email
        dto.is_superuser = user.is_superuser
        dto.groups = list([UserGroupOutDto.from_group(group) for group in user.groups.all()])
        return dto
