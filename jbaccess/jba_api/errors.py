from api_commons.error import ErrorCode

SOMETHING_WRONG = ErrorCode(0x001, "Something went wrong")
INCORRECT_CREDENTIALS = ErrorCode(0x002, "Incorrect credentials")
NOT_SUPPORTED = ErrorCode(0x003, "Not supported")
CALCULATION_FAILED = ErrorCode(0x004, "Calculation failed")
INCORRECT_CONTROLLER = ErrorCode(0x005, "Controller is invalid")
CONTROLLER_NOT_FOUND = ErrorCode(0x006, "Controller was not found")
DOOR_NOT_FOUND = ErrorCode(0x007, "Door not found")