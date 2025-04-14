from django.contrib import admin

from app.category.admin import AdditionalCategoryInline
from app.product.models import Additional, Product


@admin.register(Additional)
class AdditionalAdmin(admin.ModelAdmin):
    # Add/Change
    radio_fields = {"unit": admin.VERTICAL}

    # Change list view
    list_display = ("name", "description", "price", "created_at")
    ordering = ("-name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Add/Change
    inlines = [AdditionalCategoryInline]
    radio_fields = {"unit": admin.VERTICAL}

    # Change list view
    list_display = ("name", "price", "created_at", "updated_at")
    ordering = ("-name",)
