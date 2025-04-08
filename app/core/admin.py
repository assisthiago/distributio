from django.contrib import admin

from app.core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin interface for the User model.
    """

    list_display = ("id", "username", "email", "is_active", "is_staff")
    list_filter = ("is_active", "is_staff")
    search_fields = ("username", "email")
    ordering = ("username",)
