
from rest_framework import generics
from .models import Orders
from .serializers import OrdersSerializer

class OrdersViewSet(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer