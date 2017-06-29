from api_commons.common import ApiResponse
from django.http import HttpRequest

from jba_api import permissions
from jba_api.common import JbAccessController, dto_inject
from jba_api.controllers.dto import ControllerOutDto, ControllerInDto
from jba_core.service import ControllerService


class ControllersController(JbAccessController):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest):
        controllers = ControllerService.get_all()
        controller_dtos = list([ControllerOutDto.from_controller(c) for c in controllers])
        return ApiResponse.success(controller_dtos)

    @dto_inject(ControllerInDto)
    def post(self, request: HttpRequest, dto: ControllerInDto):
        controller = ControllerService.create(dto.name, dto.controller_id)
        return ApiResponse.success(ControllerOutDto.from_controller(controller))


class ControllersRUDController(JbAccessController):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        controller = ControllerService.get(id)
        return ApiResponse.success(ControllerOutDto.from_controller(controller))

    @dto_inject(ControllerInDto)
    def put(self, request: HttpRequest, id: str, dto: ControllerInDto):
        id = self.parse_int_pk(id)
        controller = ControllerService.update(id, name=dto.name, controller_id=dto.controller_id)
        return ApiResponse.success(ControllerOutDto.from_controller(controller))

    def delete(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        ControllerService.delete(id)
        return ApiResponse.success()
