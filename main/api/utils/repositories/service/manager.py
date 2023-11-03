from api.serializers import CalculatorSerializer
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from .abstract import AbstractServiceRepository, AbstractServiceManager
from .subservice import SubServiceRepository


class SubServiceManager(AbstractServiceManager):

    def __init__(self, repository: AbstractServiceRepository) -> None:
        self.repository = repository

    def post(self, request: Request) -> Response:
        data = CalculatorSerializer(data=request.data)
        if data.is_valid():
            response_data = self.repository.post(data=data)
            if response_data is not None:
                return Response(response_data.initial_data, status=status.HTTP_200_OK)
            return Response("invalid", status=status.HTTP_400_BAD_REQUEST)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


sub_service_manager = SubServiceManager(
    repository=SubServiceRepository()
)
