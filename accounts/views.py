from rest_framework import generics
from .models import Walet
from .serializers import WaletSerializer,UpateSerializer
from rest_framework.permissions import IsAuthenticated

class WaletListCreateView(generics.ListCreateAPIView):
    queryset = Walet.objects.all()
    serializer_class = WaletSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Walet.objects.filter(user = self.request.user)


class WaletUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Walet.objects.all()
    serializer_class = UpateSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Walet.objects.filter(user = self.request.user)



