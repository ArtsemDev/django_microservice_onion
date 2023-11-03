from rest_framework.viewsets import ViewSet

from .serializers import CalculatorSerializer
from .utils.repositories.service import sub_service_manager


class CalculatorViewSet(ViewSet):
    serializer = CalculatorSerializer

    def post(self, request):
        return sub_service_manager.post(request=request)
