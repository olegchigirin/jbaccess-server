from jba_api.common import JbAccessController, dto_inject
from jba_api import permissions
from jba_api.doors.dto import DoorOutDto
from jba_core.service import PlaceService
from api_commons.common import ApiResponse
from django.http import HttpRequest

from jba_api.places.dto import PlaceInDto, PlaceOutDto


class PlacesController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest):
        places = PlaceService.get_all()
        place_dtos = list([PlaceOutDto.from_place(p) for p in places])
        return ApiResponse.success(place_dtos)

    @dto_inject(PlaceInDto)
    def post(self, request: HttpRequest, dto: PlaceInDto):
        place = PlaceService.create(dto.name)
        return ApiResponse.success(PlaceOutDto.from_place(place))


class PlacesRUDController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        place = PlaceService.get(id)
        return ApiResponse.success(PlaceOutDto.from_place(place))

    @dto_inject(PlaceInDto)
    def put(self, request: HttpRequest, id: str, dto: PlaceInDto):
        id = self.parse_int_pk(id)
        place = PlaceService.update(id, dto.name)
        return ApiResponse.success(PlaceOutDto.from_place(place))

    def delete(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        PlaceService.delete(id)
        return ApiResponse.success()


class GetDoorsController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        doors = PlaceService.get_doors(id)
        door_dtos = list([DoorOutDto.from_door(d) for d in doors])
        return ApiResponse.success(door_dtos)


class PlacesDoorRelationController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def put(self, request: HttpRequest, place_id: str, door_id: str):
        place_id = self.parse_int_pk(place_id)
        door_id = self.parse_int_pk(door_id)
        PlaceService.attach_door(place_id, door_id)
        return ApiResponse.success()

    def delete(self, request: HttpRequest, place_id: str, door_id: str):
        place_id = self.parse_int_pk(place_id)
        door_id = self.parse_int_pk(door_id)
        PlaceService.detach_door(place_id, door_id)
        return ApiResponse.success()
