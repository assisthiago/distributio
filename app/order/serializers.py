from rest_framework import serializers

from app.client.serializers import ClientUserSerializer
from app.order.models import Order
from app.product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    user = ClientUserSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
