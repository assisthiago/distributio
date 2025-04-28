import requests
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from app.client.models import Address, Client
from app.client.serializers import (
    AddressSerializer,
    ClientSerializer,
    ClientUserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = ClientUserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """

    permission_classes = [IsAuthenticated]

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows addresses to be viewed or edited.
    """

    permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @action(
        detail=False,
        methods=["get"],
        url_path="zip-code/(?P<code>[^/.]+)",
        url_name="zip_code",
        permission_classes=[IsAuthenticatedOrReadOnly],
    )
    def get_zip_code(self, request, code):
        """
        Get zip code information from an external API.
        """
        endpoint = "https://brasilapi.com.br/api/cep/v1"  # External API endpoint
        response = requests.get(f"{endpoint}/{code}")

        if response.status_code == status.HTTP_200_OK:
            data = response.json()
            del data["service"]  # Remove the service key from the response
            return Response(data, status=status.HTTP_200_OK)

        return Response(status=response.status_code)
