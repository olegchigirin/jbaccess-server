class SomethingWrong(Exception):
    pass


class EntityNotFound(SomethingWrong):
    pass


class ControllerNotFound(EntityNotFound):
    pass


class DoorNotFound(EntityNotFound):
    pass


class EntityManageFailed(SomethingWrong):
    pass


class ControllerManageFailed(EntityManageFailed):
    pass

class DoorManageFailed(EntityManageFailed):
    pass