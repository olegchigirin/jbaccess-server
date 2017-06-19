from django.http import HttpRequest

from jba_api import errors
from api_commons.common import ApiResponse
from jba_api.calculator.dto import CalculationRequestDto, CalculationResultDto
from jba_api.common import JbAccessController
from jba_core.service import DummyCalculationService


class SumController(JbAccessController):
    def get(self, request: HttpRequest):
        return ApiResponse.not_found(errors.NOT_SUPPORTED)

    def post(self, request: HttpRequest):
        dto = CalculationRequestDto.from_dict(request.data)
        if not dto.is_valid():
            return ApiResponse.bad_request(dto)
        task = DummyCalculationService.CalculationTask(arg1=dto.arg1, arg2=dto.arg2, operator=dto.operator)
        try:
            result = DummyCalculationService.calculate(task)
            return ApiResponse.success(
                CalculationResultDto.from_calculation_result(result)
            )
        except Exception as e: # Should be more concrete
            return ApiResponse.bad_request("Unable to calculate your expression: " + str(e))