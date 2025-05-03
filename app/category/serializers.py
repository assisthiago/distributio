from rest_framework import serializers

from app.category.models import AdditionalCategory, ProductCategory
from app.product.serializers import AdditionalSerializer, ProductSerializer


class AdditionalCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for listing, creating and retrieving the AdditionalCategory model.
    """

    additionals = AdditionalSerializer(
        many=True,
        required=False,
        read_only=True,
    )

    class Meta:
        model = AdditionalCategory
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "image": {"write_only": True},
            "products": {"write_only": True},
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
