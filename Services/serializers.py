from rest_framework.serializers import ModelSerializer  
from .models import Service, Cat


class CatSerializer(ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'



class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

