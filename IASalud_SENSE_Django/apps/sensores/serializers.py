from rest_framework import serializers
from .models import Sensor
from apps.registros.serializers import RegistroSerializer

class SensorSerializer(serializers.ModelSerializer):
    registros = RegistroSerializer(many=True, required=False)
    
    class Meta:
        model = Sensor
        fields = '__all__'
        read_only_fields = ('created_at',) # No se puede modificar la fecha de creación
    
    def to_representation(self, instance):
        if instance.eliminado:  # Si el sensor está marcado como eliminado, no devolverlo en la consulta
            return None
        return super().to_representation(instance)