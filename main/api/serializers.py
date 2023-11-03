from rest_framework.serializers import Serializer
from rest_framework.fields import IntegerField


class CalculatorSerializer(Serializer):
    height = IntegerField(
        min_value=1,
    )
    width = IntegerField(
        min_value=1
    )


class CalculatorResultSerializer(CalculatorSerializer):
    result = IntegerField(
        min_value=1
    )
