from rest_framework import serializers
from .models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'nombre', 'direccion', 'numBoxes', 'created_at')
        read_only_fields = ('created_at',) # No se puede modificar la fecha de creación
        
        