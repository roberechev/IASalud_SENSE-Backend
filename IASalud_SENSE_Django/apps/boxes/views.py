from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import uuid
from .models import Box, Sensor, Paciente, Tarea
from .serializers import SensorSerializer, PacienteSerializer, TareaSerializer

@api_view(['POST'])
def add_sensor_to_box(request, box_id):
    try:
        box = Box.objects.get(pk=box_id)
    except Box.DoesNotExist:
        return Response({"error": "Box does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    id_sensor = request.data.get('id_sensor')  # Obtener el ID del sensor del cuerpo de la solicitud
    
    try:
        sensor = Sensor.objects.get(pk=id_sensor)  # Obtener el sensor correspondiente al ID proporcionado
        box.sensores.add(sensor)  # Agregar el sensor al box
        box.save()
        return Response({"message": "Sensor added to box successfully"}, status=status.HTTP_201_CREATED)
    except Sensor.DoesNotExist:
        return Response({"error": "Sensor does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'El box ya tiene asignada ese sensor.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def eliminar_sensor_of_box(request, box_id):
    try:
        box = Box.objects.get(pk=box_id)
    except Box.DoesNotExist:
        return Response({"error": "Box does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    id_sensor = request.data.get('id_sensor')
    try:
        sensor = Sensor.objects.get(pk=id_sensor)
        box.sensores.remove(sensor)
        box.save()
        return Response({"message": "Sensor removed from box successfully"}, status=status.HTTP_201_CREATED)
    except Sensor.DoesNotExist:
        return Response({"error": "Sensor does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'Fallo inesperado en el sensor (no existe ese sensor)'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def add_paciente_to_box(request, box_id):
    try:
        box = Box.objects.get(pk=box_id)
    except Box.DoesNotExist:
        return Response({"error": "Box does not exist"}, status=status.HTTP_404_NOT_FOUND)

    id_paciente = request.data.get('id_paciente')  # Obtener el ID del paciente del cuerpo de la solicitud
    
    try:
        paciente = Paciente.objects.get(pk=id_paciente)  # Obtener el paciente correspondiente al ID proporcionado
        box.paciente = paciente  # Asignar el paciente al box
        box.save()
        return Response({"message": "Paciente added to box successfully"}, status=status.HTTP_201_CREATED)
    except Paciente.DoesNotExist:
        return Response({"error": "Paciente does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def add_tarea_to_box(request, box_id):
    try:
        box = Box.objects.get(pk=box_id)
    except Box.DoesNotExist:
        return Response({"error": "Box does not exist"}, status=status.HTTP_404_NOT_FOUND)

    id_tarea = request.data.get('id_tarea')  # Obtener el ID de la tarea del cuerpo de la solicitud
    
    try:
        tarea = Tarea.objects.get(pk=id_tarea)  # Obtener la tarea correspondiente al ID proporcionado
        box.tareas.add(tarea)  # Agregar el sensor al box
        box.save()
        return Response({"message": "Tarea added to box successfully"}, status=status.HTTP_201_CREATED)
    except Tarea.DoesNotExist:
        return Response({"error": "Tarea does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'El box ya tiene asignada esa tarea.'}, status=status.HTTP_404_NOT_FOUND)

# Añade un audio al box seleccionado
@api_view(['POST'])
def upload_audio_to_box(request, box_id):
    try:
        box = Box.objects.get(pk=box_id)
    except Box.DoesNotExist:
        return Response({"error": "Box does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        
        nombreTarea = request.data.get('nombreTarea')
        nombreTarea = nombreTarea.replace(' ', '-')
        # Generar un nombre único para el archivo de audio
        audio_name = nombreTarea + str(uuid.uuid4())[:10] + '.mp3'
        # audio_name = audio_name.replace('-', '_')
        audio_file.name = audio_name
        
        # prioridad del audio
        prioridad = request.data.get('prioridad')
        print("-------p3" + prioridad)
        # Guardar el archivo de audio en el sistema de archivos del servidor
        # file_path = default_storage.save("audio/" + audio_name, ContentFile(audio_file.read()))
        
        # Comprobar si el archivo se guardó correctamente
        if audio_file:            
            # Crear un objeto File de Django para el archivo de audio
            # audio_file_object = File('audio/'+audio_name, default_storage.open(file_path, 'rb'))
            # Crear los datos de la tarea con el nombre del archivo de audio y el objeto File
            tarea_data = {
                'nombre': audio_name,  # Utilizamos el nombre del archivo de audio como nombre de la tarea
                'audio_recordatorio': audio_file,  # Asignamos el objeto File al campo de audio_recordatorio de la tarea
                "prioridad": prioridad
            }
            #audio_file_object.close()
            # Crear la tarea utilizando el serializer
            tarea_serializer = TareaSerializer(data=tarea_data)
            if tarea_serializer.is_valid():
                tarea = tarea_serializer.save()
                box.tareas.add(tarea)
                box.save()
                return Response({"message": "Audio added to box successfully"}, status=status.HTTP_201_CREATED)
            else:
                print(tarea_serializer.errors)  # Imprimir errores del serializer
                return Response(tarea_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Failed to upload audio'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({'error': 'No audio file provided'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delete_box(request, box_id):
        try:
            box = Box.objects.get(pk=box_id)
        except Paciente.DoesNotExist:
            return Response({"error": "Box does not exist"}, status=status.HTTP_404_NOT_FOUND)
        box.soft_delete()  # Marcar como eliminado
        return Response(status=status.HTTP_204_NO_CONTENT)