from .models import Registro
from rest_framework import viewsets, permissions
from .serializers import RegistroSerializer

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegistroSerializer