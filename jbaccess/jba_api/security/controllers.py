from api_commons.common import ApiResponse
from django.contrib import auth
from django.http import HttpRequest

from jba_api import permissions
from jba_api.common import JbAccessController, dto_inject
from jba_api.security.dto import LoginInDto, UserInfoOutDto
from jba_core.service import UserService


class LoginController(JbAccessController):
    @dto_inject(LoginInDto)
    def post(self, request: HttpRequest, dto: LoginInDto):
        user = UserService.get_user_by_credentials(dto.login, dto.password)
        auth.login(request, user)
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
