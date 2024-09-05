from rest_framework import serializers
from .models import Walet

class WaletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walet
        fields = '__all__'