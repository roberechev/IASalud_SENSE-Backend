from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Paciente
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def delete_paciente(request, paciente_id):
        try:
            paciente = Paciente.objects.get(pk=paciente_id)
        except Paciente.DoesNotExist:
            return Response({"error": "Paciente does not exist"}, status=status.HTTP_404_NOT_FOUND)
        paciente.soft_delete()  # Marcar como eliminado
        return Response(status=status.HTTP_204_NO_CONTENT)
