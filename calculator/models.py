from django.db import models


class Calculation(models.Model):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

    OPERATION_CHOICES = (
        (ADD, "Add"),
        (SUBTRACT, "Subtract"),
        (MULTIPLY, "Multiply"),
        (DIVIDE, "Divide"),
    )

    operand1 = models.FloatField()
    operand2 = models.FloatField()
    operation = models.CharField(max_length=20, choices=OPERATION_CHOICES)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.operand1} {self.operation} {self.operand2} = {self.result}"

    def calculate_result(self):
        operations = {
            self.ADD: self.operand1 + self.operand2,
            self.SUBTRACT: self.operand1 - self.operand2,
            self.MULTIPLY: self.operand1 * self.operand2,
            self.DIVIDE: self.operand1 / self.operand2,
        }
        return operations[self.operation]

    def save(self, *args, **kwargs):
        self.result = self.calculate_result()
        super().save(*args, **kwargs)
