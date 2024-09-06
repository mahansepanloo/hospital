from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Service, Cat
from .serializers import ServiceSerializer
from .permission import IsNurse

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from .models import Service
from .serializers import ServiceSerializer

class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]

    def get_queryset(self):
        queryset = super().get_queryset()
        date_filter = self.request.query_params.get('date', None)
        bimar_name = self.request.query_params.get('bimar_name', None)

        if date_filter:
            today = timezone.now().date()
            if date_filter == 'today':
                queryset = queryset.filter(date=today)
            elif date_filter == 'yesterday':
                yesterday = today - timedelta(days=1)
                queryset = queryset.filter(date=yesterday)
            elif date_filter == 'tomorrow':
                tomorrow = today + timedelta(days=1)
                queryset = queryset.filter(date=tomorrow)

        if bimar_name:
            queryset = queryset.filter(bimar__name__icontains=bimar_name)

        return queryset


class ServiceDetailAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]

class ServiceCreateAPIView(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]


class ServiceUpdateAPIView(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]

class ServiceDeleteAPIView(DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]

class CatListAPIView(ListAPIView):
    queryset = Cat.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]


class CatDetailAPIView(RetrieveAPIView):
    queryset = Cat.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]

class CatCreateAPIView(CreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]

class CatUpdateAPIView(UpdateAPIView):
    queryset = Cat.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]

class CatDeleteAPIView(DestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]


