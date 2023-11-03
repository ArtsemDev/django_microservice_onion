from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import CalculatorSerializer, CalculatorResultSerializer


class CalculatorViewSet(ViewSet):
    serializer = CalculatorSerializer

    def post(self, request):
        data = self.serializer(data=request.data)
        if data.is_valid():
            result = data.initial_data.get("width") * data.initial_data.get("height")
            response_data = CalculatorResultSerializer(
                data=data.initial_data | {"result": result}
            )
            return Response(response_data.initial_data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
