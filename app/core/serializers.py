from rest_framework.serializers import ModelSerializer, StringRelatedField

from app.core.models import AdditionalCategory, Item, Product, ProductCategory, User


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


class ItemSerializer(ModelSerializer):
    """
    Serializer for listing, creating and retrieving the Item model.
    """

    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "image": {"required": False},
        }


class ProductSerializer(ModelSerializer):
    """
    Serializer for listing, creating and retrieving the Product model.
    """

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "image": {"required": False},
        }


class AdditionalCategorySerializer(ModelSerializer):
    """
    Serializer for listing, creating and retrieving the AdditionalCategory model.
    """

    additionals = ItemSerializer(
        many=True,
        required=False,
        read_only=True,
    )
    product = StringRelatedField(
        required=False,
        read_only=True,
    )

    class Meta:
        model = AdditionalCategory
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "image": {"write_only": True},
            "product": {"write_only": True},
            "additionals": {"write_only": True},
        }


class ProductCategorySerializer(ModelSerializer):
    """
    Serializer for listing, creating and retrieving the ProductCategory model.
    """

    products = ProductSerializer(
        many=True,
        required=False,
        read_only=True,
    )

    class Meta:
        model = ProductCategory
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "image": {"required": False},
        }
