from rest_framework import serializers

from app.core.models import (
    AdditionalCategory,
    Address,
    Item,
    Order,
    Product,
    ProductCategory,
    User,
)


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for listing, creating and retrieving the Address model.
    """

    class Meta:
        model = Address
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for listing, creating and retrieving the User model.
    """

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
            "cpf",
            "phone",
            "birth_date",
            "addresses",
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


class ItemSerializer(serializers.ModelSerializer):
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


class ProductSerializer(serializers.ModelSerializer):
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


class AdditionalCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for listing, creating and retrieving the AdditionalCategory model.
    """

    additionals = ItemSerializer(
        many=True,
        required=False,
        read_only=True,
    )
    product = serializers.StringRelatedField(
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


class ProductCategorySerializer(serializers.ModelSerializer):
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


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for listing, creating and retrieving the Order model.
    """

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "image": {"required": False},
        }
