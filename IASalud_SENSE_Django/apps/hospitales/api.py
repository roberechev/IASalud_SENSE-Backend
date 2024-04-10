from .models import Hospital
from rest_framework import viewsets, permissions
from .serializers import HospitalSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HospitalSerializer
    