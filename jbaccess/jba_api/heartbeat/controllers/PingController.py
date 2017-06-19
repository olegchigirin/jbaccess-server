from api_commons.common import ApiResponse
from jba_api.common import JbAccessController


class PingController(JbAccessController):
    def get(self, request):
        return ApiResponse.success()