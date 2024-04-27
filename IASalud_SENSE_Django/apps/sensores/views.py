from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor, Registro
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def delete_sensor(request, sensor_id):
        try:
            sensor = Sensor.objects.get(pk=sensor_id)
        except Sensor.DoesNotExist:
            return Response({"error": "Sensor does not exist"}, status=status.HTTP_404_NOT_FOUND)
        sensor.soft_delete()  # Marcar como eliminado
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def add_registro_to_sensor(request, sensor_id):
    try:
        sensor = Sensor.objects.get(pk=sensor_id)
    except Sensor.DoesNotExist:
        return Response({"error": "Sensor does not exist"}, status=status.HTTP_404_NOT_FOUND)

    id_registro = request.data.get('id_registro')
    print("---------------------------ID DEL REGISTRO: "+str(id_registro) + " ID DEL SENSOR: "+str(sensor_id))
    try:
        registro = Registro.objects.get(pk=id_registro)  # Obtener el registro correspondiente al ID proporcionado
        sensor.registros.add(registro)  # Agregar el registro al sensor
        sensor.save()
        return Response({"message": "Registro added to sensor successfully"}, status=status.HTTP_201_CREATED)
    except Registro.DoesNotExist:
        return Response({"error": "Registro does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'El sensor ya tiene asignada ese registro.'}, status=status.HTTP_404_NOT_FOUND)