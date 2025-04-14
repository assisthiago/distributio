from django.contrib import admin

from app.core.models import (
    AdditionalCategory,
    Address,
    Item,
    Order,
    Product,
    ProductCategory,
    User,
)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    # Add/Change
    list_filter = ("user",)

    # Change list view
    list_display = ("street", "user", "city", "state", "zip_code")
    ordering = ("-user",)
    search_fields = ("user__username", "street", "city", "state", "zip_code")


class AddressInline(admin.StackedInline):

    model = Address
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    # Add/Change
    inlines = [AddressInline]

    # Change list view
    list_display = ("username", "email", "is_active", "is_staff")
    ordering = ("username",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "description", "price", "created_at")
    ordering = ("-name",)


@admin.register(AdditionalCategory)
class AdditionalCategoryAdmin(admin.ModelAdmin):

    # Add/Change
    filter_horizontal = ("additionals",)
    radio_fields = {"type": admin.HORIZONTAL}

    # Change list view
    list_display = ("title", "updated_at", "created_at")
    ordering = ("-title",)


class AdditionalCategoryInline(admin.StackedInline):

    model = AdditionalCategory
    extra = 1

    # Form
    filter_horizontal = ("additionals",)
    radio_fields = {"type": admin.HORIZONTAL}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # Add/Change
    inlines = [AdditionalCategoryInline]

    # Change list view
    list_display = ("name", "price", "created_at", "updated_at")
    ordering = ("-name",)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):

    # Add/Change
    filter_horizontal = ("products",)

    # Change list view
    list_display = ("title", "updated_at", "created_at")
    ordering = ("-title",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    # Add/Change
    filter_horizontal = ("products",)

    # Change list view
    list_display = ("user", "status", "created_at")
    ordering = ("-created_at",)
