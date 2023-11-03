from django.urls import path

from .views import CalculatorViewSet


urlpatterns = [
    path("calculator/", CalculatorViewSet.as_view({"post": "post"}))
]
