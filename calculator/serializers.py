from rest_framework import serializers

from .models import Calculation


class CalculationSerializer(serializers.ModelSerializer):
    result = serializers.FloatField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Calculation
        fields = ("id", "operand1", "operand2", "operation", "result", "created_at")
        read_only_fields = ("id", "result", "created_at")

    def validate(self, attrs):
        if attrs["operation"] == Calculation.DIVIDE and attrs["operand2"] == 0:
            raise serializers.ValidationError(
                {"operand2": "Cannot divide by zero."}
            )
        return attrs


class CalculationInputSerializer(serializers.Serializer):
    operand1 = serializers.FloatField()
    operand2 = serializers.FloatField()
    operation = serializers.ChoiceField(
        choices=Calculation.OPERATION_CHOICES
    )

    def validate(self, attrs):
        if attrs["operation"] == Calculation.DIVIDE and attrs["operand2"] == 0:
            raise serializers.ValidationError(
                {"operand2": "Cannot divide by zero."}
            )
        return attrs

    def calculate(self):
        calculation = Calculation(**self.validated_data)
        calculation.save()
        return calculation
