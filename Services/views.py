from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Service, Cat
from .serializers import ServiceSerializer
from .permission import IsNurse

class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsNurse]

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