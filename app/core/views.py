from rest_framework.viewsets import ModelViewSet

from app.core.models import AdditionalCategory, Item, Product, ProductCategory, User
from app.core.serializers import (
    AdditionalCategorySerializer,
    ItemSerializer,
    ProductCategorySerializer,
    ProductSerializer,
    UserSerializer,
    UserUpdateSerializer,
)


class UserViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "update":
            return UserUpdateSerializer
        return super().get_serializer_class()


class ItemViewSet(ModelViewSet):
    """
    A viewset for viewing and editing item instances.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ProductCategoryViewSet(ModelViewSet):
    """
    A viewset for viewing and editing product category instances.
    """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class AdditionalCategoryViewSet(ModelViewSet):
    """
    A viewset for viewing and editing additional category instances.
    """

    queryset = AdditionalCategory.objects.all()
    serializer_class = AdditionalCategorySerializer


class ProductViewSet(ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related("additional_categories")
        return queryset
