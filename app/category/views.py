from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from app.category.models import AdditionalCategory, ProductCategory
from app.category.serializers import (
    AdditionalCategorySerializer,
    ProductCategorySerializer,
)


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

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["product"]
