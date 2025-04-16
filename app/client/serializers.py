from django.contrib.auth.models import User
from rest_framework import serializers

from app.client.models import Address, Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ["user"]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ["user"]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class ClientUserSerializer(serializers.ModelSerializer):
    """
    Serializer for listing, creating and retrieving the User model.
    """

    client = ClientSerializer(
        many=False,
        required=False,
        read_only=True,
    )
    addresses = AddressSerializer(
        many=True,
        required=False,
        read_only=True,
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "client",
            "addresses",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
        }
