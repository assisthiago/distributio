from django.contrib import admin

from app.category.models import AdditionalCategory, ProductCategory


@admin.register(AdditionalCategory)
class AdditionalCategoryAdmin(admin.ModelAdmin):
    # Add/Change
    filter_horizontal = ("additionals", "products")
    radio_fields = {"type": admin.HORIZONTAL}

    # Change list view
    list_display = (
        "title",
        "order",
        "type",
        "show",
        "required",
        "updated_at",
    )
    list_editable = (
        "order",
        "show",
        "required",
    )
    ordering = ("order", "title")


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    # Add/Change
    filter_horizontal = ("products",)

    # Change list view
    list_display = ("title", "updated_at", "created_at")
    ordering = ("-title",)
