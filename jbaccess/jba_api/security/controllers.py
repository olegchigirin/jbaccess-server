from api_commons.common import ApiResponse
from django.contrib import auth
from django.http import HttpRequest

from jba_api import errors
from jba_api import permissions
from jba_api.common import JbAccessController
from jba_api.security.dto import LoginInDto, UserInfoOutDto
from jba_core.service import UserService


class LoginController(JbAccessController):
    def post(self, request: HttpRequest):
        dto = LoginInDto.from_dict(request.data)
        if not dto.is_valid():
            return ApiResponse.bad_request(dto)
        user = UserService.get_user_by_credentials(dto.login, dto.password)
        if user is None:
            return ApiResponse.not_found(errors.INCORRECT_CREDENTIALS)
        return ApiResponse.success(UserInfoOutDto.from_user(user))


class LogoutController(JbAccessController):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest):
        auth.logout(request)
        return ApiResponse.success()


class RestoreSessionController(JbAccessController):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest):
        user = auth.get_user(request)
        return ApiResponse.success(UserInfoOutDto.from_user(user))
