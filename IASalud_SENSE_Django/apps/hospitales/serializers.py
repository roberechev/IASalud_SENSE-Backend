from rest_framework import serializers
from .models import Hospital, Box, Paciente
from apps.boxes.serializers import BoxSerializer
from apps.pacientes.serializers import PacienteSerializer

class HospitalSerializer(serializers.ModelSerializer):
    pacientes = PacienteSerializer(many=True, required=False)  # Serialización anidada de los pacientes
    boxes = BoxSerializer(many=True, required=False)  # Serialización anidada de los sensores
    
    class Meta:
        model = Hospital
        fields = '__all__'
        read_only_fields = ('created_at',) # No se puede modificar la fecha de creación       