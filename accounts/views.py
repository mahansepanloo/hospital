from rest_framework import generics
from .models import Walet
from .serializers import WaletSerializer

class WaletListCreateView(generics.ListCreateAPIView):
    queryset = Walet.objects.all()
    serializer_class = WaletSerializer

class WaletDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Walet.objects.all()
    serializer_class = WaletSerializer