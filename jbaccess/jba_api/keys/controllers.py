from api_commons.common import ApiResponse
from django.http import HttpRequest
from jba_api.common import JbAccessController, dto_inject
from jba_api import permissions
from jba_api.keys.dto import KeyInDto, KeyOutDto
from jba_core.service import KeyService


class KeysController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest):
        keys = KeyService.get_all()
        key_dtos = list([KeyOutDto.from_key(k) for k in keys])
        return ApiResponse.success(key_dtos)

    @dto_inject(KeyInDto)
    def post(self, request: HttpRequest, dto: KeyInDto):
        key = KeyService.create(dto.name, dto.access_key, dto.person_id)
        return ApiResponse.success(KeyOutDto.from_key(key))


class KeysRUDController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        key = KeyService.get(id)
        return ApiResponse.success(KeyOutDto.from_key(key))

    @dto_inject(KeyInDto)
    def put(self, request: HttpRequest, id: str, dto: KeyInDto):
        id = self.parse_int_pk(id)
        key = KeyService.update(id, dto.name, dto.access_key, dto.person_id)
        return ApiResponse.success(KeyOutDto.from_key(key))

    def delete(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        KeyService.delete(id)
        return ApiResponse.success()
