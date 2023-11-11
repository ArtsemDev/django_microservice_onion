from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers import CalculatorSerializer
from .abstract import AbstractServiceManager
from .manager import sub_service_manager


class UnitOfWorkService(AbstractServiceManager):

    def __init__(self, services: dict[str, AbstractServiceManager]):
        self.services = services

    def post(self, request: Request) -> Response:
        data = CalculatorSerializer(data=request.data)
        if data.is_valid():
            service = self.services.get(data.initial_data.get("action"))
            return service.post(request=request)
        return Response(data="invalid data", status=422)


uow_service = UnitOfWorkService(
    services={
        "sum": sub_service_manager,
    }
)
