from rest_framework import serializers
from .models import Box, Sensor, Tarea, Paciente
from apps.sensores.serializers import SensorSerializer
from apps.tareas.serializers import TareaSerializer
from apps.pacientes.serializers import PacienteSerializer

class BoxSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(required=False)         # Serialización del paciente asociado
    sensores = SensorSerializer(many=True, required=False)  # Serialización anidada de los sensores
    tareas = TareaSerializer(many=True, required=False)     # Serialización anidada de las tareas

    class Meta:
        model = Box
        fields = '__all__'
        read_only_fields = ('created_at',) # No se puede modificar la fecha de creación