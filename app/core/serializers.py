from rest_framework.serializers import ModelSerializer

from app.core.models import User


class UserSerializer(ModelSerializer):
    """
    Serializer for listing, creating and retrieving the User model.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "cpf",
            "phone",
            "birth_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "password": {"write_only": True},
        }


class UserUpdateSerializer(UserSerializer):
    """
    Serializer for updating the User model.
    """

    class Meta(UserSerializer.Meta):
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
        }
