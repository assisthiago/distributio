from django.contrib import admin

from app.core.models import Item, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ("username", "email", "is_active", "is_staff")
    ordering = ("username",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "description", "price", "created_at")
    ordering = ("-name",)
