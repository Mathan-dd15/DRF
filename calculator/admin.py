from django.contrib import admin

from .models import Calculation


@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    list_display = ("id", "operand1", "operation", "operand2", "result", "created_at")
    list_filter = ("operation", "created_at")
    search_fields = ("operation",)
    readonly_fields = ("result", "created_at")
