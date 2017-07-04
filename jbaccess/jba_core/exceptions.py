class SomethingWrong(Exception):
    pass


class EntityNotFound(SomethingWrong):
    pass


class ControllerNotFound(EntityNotFound):
    pass


class DoorNotFound(EntityNotFound):
    pass


class PlaceNotFound(EntityNotFound):
    pass


class PersonNotFound(EntityNotFound):
    pass


class KeyNotFound(EntityNotFound):
    pass


class RoleNotFound(EntityNotFound):
    pass


class ACLNotFound(EntityNotFound):
    pass


class PatternNotFound(EntityNotFound):
    pass


class EntityManageFailed(SomethingWrong):
    pass


class ControllerManageFailed(EntityManageFailed):
    pass


class DoorManageFailed(EntityManageFailed):
    pass


class PlaceManageFailed(EntityManageFailed):
    pass


class PersonManageFailed(EntityManageFailed):
    pass


class KeyManageFailed(EntityManageFailed):
    pass


class RoleManageFailed(EntityManageFailed):
    pass


class ACLManageFailed(EntityManageFailed):
    pass


class PatternManageFailed(EntityManageFailed):
    pass


class PatternTimingIncorrect(EntityManageFailed):
    pass


class PatternDatesIncorrect(EntityManageFailed):
    pass


class AclAlreadyAdded(EntityManageFailed):
    pass
