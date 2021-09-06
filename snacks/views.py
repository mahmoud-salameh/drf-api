from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Snack
from .serializers import SnackSerializer
from .permissions import IsOwnerOrReadOnly

class SnacksList(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnacksDetail(RetrieveUpdateDestroyAPIView):

    permission_classes = (IsOwnerOrReadOnly)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer