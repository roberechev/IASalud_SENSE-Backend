from rest_framework import serializers
from .models import Registro

class RegistroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Registro
        fields = '__all__'
        read_only_fields = ('created_at',) # No se puede modificar la fecha de creación