from django.http import HttpRequest
from api_commons.common import ApiResponse

from jba_api import permissions
from jba_api.acls.dto import RoleAclOutDto
from jba_api.common import JbAccessController, dto_inject
from jba_api.roles.dto import RoleInDto, RoleOutDto
from jba_core.service import RoleService, AclService


class RolesController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest):
        roles = RoleService.get_all()
        role_dtos = list([RoleOutDto.from_role(r) for r in roles])
        return ApiResponse.success(role_dtos)

    @dto_inject(RoleInDto)
    def post(self, request: HttpRequest, dto: RoleInDto):
        role = RoleService.create(dto.name)
        return ApiResponse.success(RoleOutDto.from_role(role))


class RolesRUDController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        role = RoleService.get(id)
        return ApiResponse.success(RoleOutDto.from_role(role))

    @dto_inject(RoleInDto)
    def put(self, request: HttpRequest, id: str, dto: RoleInDto):
        id = self.parse_int_pk(id)
        role = RoleService.update(id, dto.name)
        return ApiResponse.success(RoleOutDto.from_role(role))

    def delete(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        RoleService.delete(id)
        return ApiResponse.success()


class RolePlaceGetAclsController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        acls = AclService.get_role_acls(id)
        acl_dtos = list([RoleAclOutDto.from_role_acl(a) for a in acls])
        return ApiResponse.success(acl_dtos)


class RoleAllowPlaceController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def put(self, request: HttpRequest, role_id: str, place_id: str):
        role_id = self.parse_int_pk(role_id)
        place_id = self.parse_int_pk(place_id)
        acl = AclService.role_allow_place(role_id, place_id)
        return ApiResponse.success(RoleAclOutDto.from_role_acl(acl))


class RoleDenyPlaceController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def put(self, request: HttpRequest, role_id: str, place_id: str):
        role_id = self.parse_int_pk(role_id)
        place_id = self.parse_int_pk(place_id)
        acl = AclService.role_deny_place(role_id, place_id)
        return ApiResponse.success(RoleAclOutDto.from_role_acl(acl))
