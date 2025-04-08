from rest_framework.viewsets import ModelViewSet

from app.core.models import User
from app.core.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
