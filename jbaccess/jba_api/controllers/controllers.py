from api_commons.common import ApiResponse
from django.http import HttpRequest

from jba_api import permissions
from jba_api.common import JbAccessController, dto_inject
from jba_api.controllers.dto import ControllerOutDto, ControllerInDto
from jba_api.doors.dto import DoorOutDto
from jba_core.service import ControllerService


class ControllersController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest):
        controllers = ControllerService.get_all()
        controller_dtos = list([ControllerOutDto.from_controller(c) for c in controllers])
        return ApiResponse.success(controller_dtos)

    @dto_inject(ControllerInDto)
    def post(self, request: HttpRequest, dto: ControllerInDto):
        controller = ControllerService.create(dto.name, dto.controller_id)
        return ApiResponse.success(ControllerOutDto.from_controller(controller))


class ControllersRUDController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

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


class GetDoorsController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        doors = ControllerService.get_attached_doors(id)
        door_dtos = list([DoorOutDto.from_door(d) for d in doors])
        return ApiResponse.success(door_dtos)


class ControllerDoorRelationController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def put(self, request: HttpRequest, controller_id: str, door_id: str):
        controller_id = self.parse_int_pk(controller_id)
        door_id = self.parse_int_pk(door_id)
        ControllerService.attach_door(controller_id, door_id)
        return ApiResponse.success()

    def delete(self, request: HttpRequest, controller_id: str, door_id: str):
        controller_id = self.parse_int_pk(controller_id)
        door_id = self.parse_int_pk(door_id)
        ControllerService.detach_door(controller_id, door_id)
        return ApiResponse.success()
