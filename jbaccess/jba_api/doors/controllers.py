from django.http import HttpRequest
from jba_api.common import JbAccessController, dto_inject
from api_commons.common import ApiResponse
from jba_api import permissions
from jba_api.doors.dto import DoorInDto, DoorOutDto
from jba_core.service import DoorService


class DoorsController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest):
        doors = DoorService.get_all()
        doors_dto = list([DoorOutDto.from_door(d) for d in doors])
        return ApiResponse.success(doors_dto)

    @dto_inject(DoorInDto)
    def post(self, request: HttpRequest, dto: DoorInDto):
        door = DoorService.create(dto.name, dto.access_id)
        return ApiResponse.success(DoorOutDto.from_door(door))


class DoorsRUDController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        door = DoorService.get(id)
        return ApiResponse.success(DoorOutDto.from_door(door))

    @dto_inject(DoorInDto)
    def put(self, request: HttpRequest, id: str, dto: DoorInDto):
        id = self.parse_int_pk(id)
        door = DoorService.update(id, dto.name, dto.access_id)
        return ApiResponse.success(DoorOutDto.from_door(door))

    def delete(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        DoorService.delete(id)
        return ApiResponse.success()
