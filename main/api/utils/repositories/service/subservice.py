from django.conf import settings
from rest_framework import status
from rest_framework.serializers import Serializer
from httpx import Client, Response

from .abstract import AbstractServiceRepository
from api.serializers import CalculatorResultSerializer, CalculatorSerializer


class SubServiceRepository(AbstractServiceRepository):
    BASE_URL: str = f"http://{settings.SUBSERVICE_URL}:{settings.SUBSERVICE_PORT}/api/"
    CALCULATOR_ENDPOINT: str = "calculator/"

    def request(self, method: str, url: str, **kwargs) -> Response:
        with Client() as client:
            return client.request(
                method=method,
                url=self.BASE_URL + url,
                **kwargs
            )

    def post(self, data: CalculatorSerializer) -> CalculatorResultSerializer:
        response = self.request(
            method="POST",
            url=self.CALCULATOR_ENDPOINT,
            json=data.initial_data
        )
        if response.status_code == status.HTTP_200_OK:
            response = CalculatorResultSerializer(data=response.json())
            if response.is_valid():
                return response
