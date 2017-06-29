from typing import Type

from api_commons.common import BaseController, ApiResponse
from api_commons.dto import BaseDto

from api_commons.common import exception_handler

from jba_core import exceptions
from jba_api import errors


class JbAccessController(BaseController):
    pass


def dto_inject(dto_class: Type[BaseDto], dto_object_name: str='dto'):
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
    return exception_handler(exc, context)
