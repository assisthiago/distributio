from rest_framework.viewsets import ModelViewSet

from app.core.models import Item, User
from app.core.serializers import ItemSerializer, UserSerializer, UserUpdateSerializer


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
