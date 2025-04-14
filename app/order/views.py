from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from app.order.models import Order
from app.order.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Order model.
    """

    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]
