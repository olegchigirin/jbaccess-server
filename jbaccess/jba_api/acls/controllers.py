from api_commons.common import ApiResponse
from django.http import HttpRequest
from jba_api import permissions
from jba_api.acls.dto import SimplePatternInDto, SimplePatternOutDto
from jba_api.common import JbAccessController, dto_inject
from jba_core.service import AclService


class DeleteAclController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def delete(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        AclService.delete_acl(id)
        return ApiResponse.success()


class AclPatternsCRController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    def get(self, request: HttpRequest, id: str):
        id = self.parse_int_pk(id)
        patterns = AclService.get_patterns(id)
        pattern_dtos = list([SimplePatternOutDto.from_simple_pattern(p) for p in patterns])
        return ApiResponse.success(pattern_dtos)

    @dto_inject(SimplePatternInDto)
    def post(self, request: HttpRequest, id: str, dto: SimplePatternInDto):
        id = self.parse_int_pk(id)
        pattern = AclService.create_pattern(id, dto.validated_data['from_time'], dto.validated_data['until_time'],
                                            dto.days_of_week, dto.days_of_month, dto.months)
        return ApiResponse.success(SimplePatternOutDto.from_simple_pattern(pattern))


class AclPatternsUDController(JbAccessController):
    permission_classes = [permissions.JbAccessPermission]

    @dto_inject(SimplePatternInDto)
    def put(self, request: HttpRequest, pattern_id: str, dto: SimplePatternInDto):
        pattern_id = self.parse_int_pk(pattern_id)
        pattern = AclService.update_pattern(pattern_id, dto.validated_data['from_time'],
                                            dto.validated_data['until_time'],
                                            dto.days_of_week, dto.days_of_month, dto.months)
        return ApiResponse.success(SimplePatternOutDto.from_simple_pattern(pattern))

    def delete(self, request: HttpRequest, pattern_id: str):
        pattern_id = self.parse_int_pk(pattern_id)
        AclService.delete_pattern(pattern_id)
        return ApiResponse.success()
