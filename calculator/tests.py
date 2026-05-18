from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Calculation


class CalculateAPITests(APITestCase):
    def test_addition(self):
        response = self.client.post(
            reverse("calculate"),
            {"operand1": 10, "operand2": 5, "operation": "add"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["result"], 15)
        self.assertEqual(Calculation.objects.count(), 1)

    def test_subtraction(self):
        response = self.client.post(
            reverse("calculate"),
            {"operand1": 10, "operand2": 5, "operation": "subtract"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["result"], 5)

    def test_multiplication(self):
        response = self.client.post(
            reverse("calculate"),
            {"operand1": 10, "operand2": 5, "operation": "multiply"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["result"], 50)

    def test_division(self):
        response = self.client.post(
            reverse("calculate"),
            {"operand1": 10, "operand2": 5, "operation": "divide"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["result"], 2)

    def test_division_by_zero_returns_validation_error(self):
        response = self.client.post(
            reverse("calculate"),
            {"operand1": 10, "operand2": 0, "operation": "divide"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("operand2", response.data)
        self.assertEqual(Calculation.objects.count(), 0)

    def test_calculation_history(self):
        Calculation.objects.create(operand1=10, operand2=5, operation=Calculation.ADD)

        response = self.client.get(reverse("calculation-history"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["result"], 15)

    def test_calculation_detail(self):
        calculation = Calculation.objects.create(
            operand1=10,
            operand2=5,
            operation=Calculation.MULTIPLY,
        )

        response = self.client.get(
            reverse("calculation-detail", kwargs={"pk": calculation.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["result"], 50)

    def test_database_details(self):
        Calculation.objects.create(operand1=10, operand2=5, operation=Calculation.ADD)
        Calculation.objects.create(
            operand1=10,
            operand2=5,
            operation=Calculation.SUBTRACT,
        )

        response = self.client.get(reverse("database-details"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_records"], 2)
        self.assertEqual(len(response.data["records"]), 2)
