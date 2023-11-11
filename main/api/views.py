from rest_framework.viewsets import ViewSet

from .serializers import CalculatorSerializer
from .utils.repositories.service import uow_service


class CalculatorViewSet(ViewSet):
    serializer = CalculatorSerializer

    def post(self, request):
        return uow_service.post(request=request)
