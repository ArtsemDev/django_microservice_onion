from abc import ABC, abstractmethod

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer


class AbstractServiceRepository(ABC):

    @abstractmethod
    def post(self, data: Serializer) -> Serializer:
        raise NotImplementedError


class AbstractServiceManager(ABC):

    @abstractmethod
    def post(self, request: Request) -> Response:
        raise NotImplementedError
