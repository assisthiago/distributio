from django.contrib import admin

from app.client.models import Address, Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "cpf",
        "user",
        "phone",
        "birth_date",
        "created_at",
        "updated_at",
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "street",
        "number",
        "neighborhood",
        "city",
        "state",
        "zip_code",
        "created_at",
        "updated_at",
    )
