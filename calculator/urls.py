from django.urls import path

from .views import (
    CalculateAPIView,
    CalculationDetailAPIView,
    CalculationHistoryAPIView,
    DatabaseDetailsAPIView,
)

urlpatterns = [
    path("calculate/", CalculateAPIView.as_view(), name="calculate"),
    path("calculations/", CalculationHistoryAPIView.as_view(), name="calculation-history"),
    path("database-details/", DatabaseDetailsAPIView.as_view(), name="database-details"),
    path(
        "calculations/<int:pk>/",
        CalculationDetailAPIView.as_view(),
        name="calculation-detail",
    ),
]
