from .models import Box
from rest_framework import viewsets, permissions
from .serializers import BoxSerializer

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BoxSerializer