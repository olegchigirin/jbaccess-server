from api_commons.error import ErrorCode
from jba_core import errors


class JbAccessException(Exception):
    def __init__(self, error_code: ErrorCode):
        self.error_code = error_code


class SomethingWrong(JbAccessException):
    def __init__(self):
        super().__init__(errors.SOMETHING_WRONG)


class BadDataException(JbAccessException):
    pass


class IncorrectCredentials(BadDataException):
    def __init__(self):
        super().__init__(errors.INCORRECT_CREDENTIALS)


class EntityNotFound(JbAccessException):
    pass


class UserNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(errors.USER_NOT_FOUND)


class ControllerNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(errors.CONTROLLER_NOT_FOUND)


class DoorNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(errors.DOOR_NOT_FOUND)


class PlaceNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(errors.PLACE_NOT_FOUND)


class PersonNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(errors.PERSON_NOT_FOUND)


class KeyNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(errors.KEY_NOT_FOUND)


class RoleNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(errors.ROLE_NOT_FOUND)


class ACLNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(errors.ACL_NOT_FOUND)


class PatternNotFound(EntityNotFound):
    def __init__(self):
        super().__init__(errors.PATTERN_NOT_FOUND)


class EntityManageFailed(BadDataException):
    pass


class ControllerManageFailed(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.CONTROLLER_MANAGE_FAILED)


class DoorManageFailed(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.DOOR_MANAGE_FAILED)


class PlaceManageFailed(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.PLACE_MANAGE_FAILED)


class PersonManageFailed(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.PERSON_MANAGE_FAILED)


class KeyManageFailed(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.KEY_MANAGE_FAILED)


class RoleManageFailed(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.ROLE_MANAGE_FAILED)


class ACLManageFailed(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.ACL_MANAGE_FAILED)


class PatternManageFailed(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.PATTERN_MANAGE_FAILED)


class PatternTimingIncorrect(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.PATTERN_TIMINGS_INCORRECT)


class PatternDatesIncorrect(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.DATE_PATTERNS_INCORRECT)


class AclAlreadyAdded(EntityManageFailed):
    def __init__(self):
        super().__init__(errors.ACL_ALREADY_ADDED)
