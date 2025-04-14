from rest_framework import serializers

from app.product.models import Additional, Product


class AdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additional
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
