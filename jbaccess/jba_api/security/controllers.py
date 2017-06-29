from api_commons.common import ApiResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest

from jba_api import errors
from jba_api import permissions
from jba_api.common import JbAccessController
from jba_api.security.dto import LoginInDto, UserInfoOutDto


class LoginController(JbAccessController):
    def post(self, request: HttpRequest):
        dto = LoginInDto.from_dict(request.data)
        if not dto.is_valid():
            return ApiResponse.bad_request(dto)
        try:
            user = User.objects.get(username=dto.login)
            if not user.check_password(dto.password):
                return ApiResponse.not_found(errors.INCORRECT_CREDENTIALS)
            auth.login(request, user)
            return ApiResponse.success(UserInfoOutDto.from_user(user))
        except:
            return ApiResponse.not_found(errors.INCORRECT_CREDENTIALS)


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
