from django.contrib import admin

from app.order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Add/Change
    filter_horizontal = ("products",)

    # Change list view
    list_display = ("number", "user", "status", "created_at")
    ordering = ("-created_at",)
