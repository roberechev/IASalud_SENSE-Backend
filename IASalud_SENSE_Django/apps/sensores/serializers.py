from rest_framework import serializers
from .models import Sensor
from apps.registros.serializers import RegistroSerializer

class SensorSerializer(serializers.ModelSerializer):
    registros = RegistroSerializer(many=True, required=False)
    
    class Meta:
        model = Sensor
        fields = '__all__'
        read_only_fields = ('created_at',) # No se puede modificar la fecha de creación