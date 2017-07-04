from typing import Type

from api_commons.common import BaseController, ApiResponse
from api_commons.common import exception_handler
from api_commons.dto import BaseDto

from jba_core import exceptions, errors


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
    if isinstance(exc, exceptions.EntityNotFound):
        return ApiResponse.not_found(exc.error_code)
    if isinstance(exc, exceptions.BadDataException):
        return ApiResponse.bad_request(exc.error_code.dto_or_error_message, exc.error_code.error_code)
    if isinstance(exc, exceptions.JbAccessException):
        return ApiResponse.bad_request(exc.error_code.dto_or_error_message, exc.error_code.error_code)
    return exception_handler(exc, context)
