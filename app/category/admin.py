from django.contrib import admin

from app.category.models import AdditionalCategory, ProductCategory


@admin.register(AdditionalCategory)
class AdditionalCategoryAdmin(admin.ModelAdmin):
    # Add/Change
    filter_horizontal = ("additionals",)
    radio_fields = {"type": admin.HORIZONTAL}

    # Change list view
    list_display = ("title", "updated_at", "created_at")
    ordering = ("-title",)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    # Add/Change
    filter_horizontal = ("products",)

    # Change list view
    list_display = ("title", "updated_at", "created_at")
    ordering = ("-title",)


# Inlines
class AdditionalCategoryInline(admin.StackedInline):
    model = AdditionalCategory
    extra = 1

    # Form
    filter_horizontal = ("additionals",)
    radio_fields = {"type": admin.HORIZONTAL}
