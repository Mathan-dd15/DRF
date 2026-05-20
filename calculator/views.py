from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Calculation
from .serializers import CalculationInputSerializer, CalculationSerializer


class CalculateAPIView(APIView):
    serializer_class = CalculationInputSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        calculation = serializer.calculate()

        return Response(
            CalculationSerializer(calculation).data,
            status=status.HTTP_201_CREATED,
        )


class CalculationHistoryAPIView(ListAPIView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer


class CalculationDetailAPIView(RetrieveAPIView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer


class DatabaseDetailsAPIView(APIView):
    def get(self, request):
        calculations = Calculation.objects.all()
        serializer = CalculationSerializer(calculations, many=True)

        return Response(
            {
                "total_records": calculations.count(),
                "records": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class HelloMathanAPIView(APIView):
    def get(self, request):
        return Response(" Hello mathan", status=status.HTTP_200_OK)
