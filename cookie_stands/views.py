from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import ThingSerializer


class CookieList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = ThingSerializer


class CookieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = ThingSerializer
