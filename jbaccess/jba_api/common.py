from typing import Type
from api_commons.common import BaseController, ApiResponse
from api_commons.common import exception_handler
from api_commons.dto import BaseDto
from jba_api import errors
from jba_core import exceptions


class JbAccessController(BaseController):
    pass


def dto_inject(dto_class: Type[BaseDto], dto_object_name: str = 'dto'):
    def dto_decorator(func):
        def wrapped(*args, **kwargs):
            request = args[1]
            dto_object = dto_class.from_dict(request.data)
            if not dto_object.is_valid():
                return ApiResponse.bad_request(dto_object)
            kwargs.setdefault(dto_object_name, dto_object)
            return func(*args, **kwargs)

        return wrapped

    return dto_decorator


def jb_exception_handler(exc, context):
    if isinstance(exc, exceptions.ControllerNotFound):
        return ApiResponse.not_found(errors.CONTROLLER_NOT_FOUND)
    if isinstance(exc, exceptions.DoorNotFound):
        return ApiResponse.not_found(errors.DOOR_NOT_FOUND)
    if isinstance(exc, exceptions.PlaceNotFound):
        return ApiResponse.not_found(errors.PLACE_NOT_FOUND)
    if isinstance(exc, exceptions.PersonNotFound):
        return ApiResponse.not_found(errors.PERSON_NOT_FOUND)
    if isinstance(exc, exceptions.KeyNotFound):
        return ApiResponse.not_found(errors.KEY_NOT_FOUND)
    if isinstance(exc, exceptions.RoleNotFound):
        return ApiResponse.not_found(errors.ROLE_NOT_FOUND)
    if isinstance(exc, exceptions.ACLNotFound):
        return ApiResponse.not_found(errors.ACL_NOT_FOUND)
    if isinstance(exc, exceptions.PatternNotFound):
        return ApiResponse.not_found(errors.PATTERN_NOT_FOUND)

    if isinstance(exc, exceptions.ControllerManageFailed):
        return ApiResponse.bad_request(errors.CONTROLLER_MANAGE_FAILED.dto_or_error_message,
                                       errors.CONTROLLER_MANAGE_FAILED.error_code)
    if isinstance(exc, exceptions.DoorManageFailed):
        return ApiResponse.bad_request(errors.DOOR_MANAGE_FAILED.dto_or_error_message,
                                       errors.DOOR_MANAGE_FAILED.error_code)
    if isinstance(exc, exceptions.PlaceManageFailed):
        return ApiResponse.bad_request(errors.PLACE_MANAGE_FAILED.dto_or_error_message,
                                       errors.PLACE_MANAGE_FAILED.error_code)
    if isinstance(exc, exceptions.PersonManageFailed):
        return ApiResponse.bad_request(errors.PERSON_MANAGE_FAILED.dto_or_error_message,
                                       errors.PERSON_MANAGE_FAILED.error_code)
    if isinstance(exc, exceptions.KeyManageFailed):
        return ApiResponse.bad_request(errors.KEY_MANAGE_FAILED.dto_or_error_message,
                                       errors.KEY_MANAGE_FAILED.error_code)
    if isinstance(exc, exceptions.RoleManageFailed):
        return ApiResponse.bad_request(errors.ROLE_MANAGE_FAILED.dto_or_error_message,
                                       errors.ROLE_MANAGE_FAILED.error_code)
    if isinstance(exc, exceptions.ACLManageFailed):
        return ApiResponse.bad_request(errors.ACL_MANAGE_FAILED.dto_or_error_message,
                                       errors.ACL_MANAGE_FAILED.error_code)
    if isinstance(exc, exceptions.PatternManageFailed):
        return ApiResponse.bad_request(errors.PATTERN_MANAGE_FAILED.dto_or_error_message,
                                       errors.PATTERN_MANAGE_FAILED.error_code)
    if isinstance(exc, exceptions.PatternTimingIncorrect):
        return ApiResponse.bad_request(errors.PATTERN_TIMINGS_INCORRECT.dto_or_error_message,
                                       errors.PATTERN_TIMINGS_INCORRECT.error_code)
    if isinstance(exc, exceptions.PatternDatesIncorrect):
        return ApiResponse.bad_request(errors.DATE_PATTERNS_INCORRECT.dto_or_error_message,
                                       errors.DATE_PATTERNS_INCORRECT.error_code)
    if isinstance(exc, exceptions.AclAlreadyAdded):
        return ApiResponse.bad_request(errors.ACL_ALREADY_ADDED.dto_or_error_message,
                                       errors.ACL_ALREADY_ADDED.error_code)
    return exception_handler(exc, context)
