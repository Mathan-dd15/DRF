from django.urls import path

from .views import (
    CalculateAPIView,
    CalculationDetailAPIView,
    CalculationHistoryAPIView,
    DatabaseDetailsAPIView,
    HelloMathanAPIView,
)

urlpatterns = [
    path("hello-mathan/", HelloMathanAPIView.as_view(), name="hello-mathan"),
    path("calculate/", CalculateAPIView.as_view(), name="calculate"),
    path("calculations/", CalculationHistoryAPIView.as_view(), name="calculation-history"),
    path("database-details/", DatabaseDetailsAPIView.as_view(), name="database-details"),
    path(
        "calculations/<int:pk>/",
        CalculationDetailAPIView.as_view(),
        name="calculation-detail",
    ),
]
