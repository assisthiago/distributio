from rest_framework import viewsets

from app.core.models import (
    AdditionalCategory,
    Address,
    Item,
    Order,
    Product,
    ProductCategory,
    User,
)
from app.core.serializers import (
    AdditionalCategorySerializer,
    AddressSerializer,
    ItemSerializer,
    OrderSerializer,
    ProductCategorySerializer,
    ProductSerializer,
    UserSerializer,
    UserUpdateSerializer,
)


class AddressViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing address instances.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        queryset = queryset.select_related("user")
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "update":
            return UserUpdateSerializer
        return super().get_serializer_class()


class ItemViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing item instances.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product category instances.
    """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class AdditionalCategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing additional category instances.
    """

    queryset = AdditionalCategory.objects.all()
    serializer_class = AdditionalCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related("additional_categories")
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing order instances.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        queryset = queryset.select_related("user")
        return queryset
