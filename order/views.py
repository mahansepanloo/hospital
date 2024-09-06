from rest_framework import generics
from .models import Orders
from .serializers import OrdersSerializer
from .permissions import IsSuperUser

class OrdersViewSet(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsSuperUser]

