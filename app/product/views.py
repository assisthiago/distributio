from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from app.product.models import Additional, Product
from app.product.serializers import AdditionalSerializer, ProductSerializer


class AdditionalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows additionals to be viewed or edited.
    """

    permission_classes = [IsAuthenticated]

    queryset = Additional.objects.all()
    serializer_class = AdditionalSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """

    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
