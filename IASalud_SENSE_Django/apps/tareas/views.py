from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import speech_recognition as sr
from .models import Tarea
from pydub import AudioSegment
import os
import subprocess
from django.core.files import File

@api_view(['GET'])
def transcripcion_audio_texto(request, tarea_id):
    try:
        tarea = Tarea.objects.get(pk=tarea_id)
    except Tarea.DoesNotExist:
        return Response({"error": "Tarea does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    audio_file = tarea.audio_recordatorio.path  # Ruta al archivo de audio

    # Ruta para el archivo WAV convertido
    wav_audio_file = os.path.splitext(audio_file)[0] + ".wav"

    ffmpeg_path = "C:\\Users\\rober\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe"
    # Comando para convertir el archivo de audio de MP3 a WAV usando ffmpeg
    command = [ffmpeg_path, '-y','-i', audio_file, wav_audio_file] # -y para sobreescribir el archivo si ya existe
    # Ejecutar el comando ffmpeg
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        return Response({"error": "Error al convertir el archivo de audio"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Realizar la transcripción del audio WAV
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_audio_file) as source:
        audio = recognizer.record(source)
    try:
        texto_transcrito = recognizer.recognize_google(audio, language='es-ES')
        return Response({"texto_transcrito": texto_transcrito}, status=status.HTTP_200_OK)
    except sr.UnknownValueError:
        return Response({"error": "No se pudo transcribir el audio"}, status=status.HTTP_404_NOT_FOUND)
    except sr.RequestError:
        return Response({"error": "Error en la solicitud al servicio de reconocimiento de voz"}, status=status.HTTP_400_BAD_REQUEST)
   
    
    # print("------------------- llego aqui 2" + tarea.audio_recordatorio.path)
    # print("------------------- llego aqui 3" + tarea.audio_recordatorio.url)
    # # Cargar el archivo MP3
    # recortarNombre = tarea.audio_recordatorio.url.split('.mp3')[0]
    # print("------------------- llego aqui 4" + recortarNombre)
    # print(os.getcwd())
    # sound = AudioSegment.from_mp3(tarea.audio_recordatorio) 
    # sound.export("aaaaaaaaaaabbbbbbbbbbbb.wav", format="wav") 
    
    # # Verificar si la tarea tiene un archivo de audio adjunto
    # if tarea.audio_recordatorio:
    #     audio_file = tarea.audio_recordatorio.path
    #     # Inicializar el reconocedor de voz
    #     recognizer = sr.Recognizer()

    #     # Intentar transcribir el audio a texto
    #     try:
    #         with sr.AudioFile(audio_file) as source:
    #             audio = recognizer.record(source)
    #         texto_transcrito = recognizer.recognize_google(audio, language='es-ES')
    #         return Response(texto_transcrito, status=status.HTTP_200_OK)
    #     except sr.UnknownValueError:
    #         return Response("No se pudo transcribir el audio", status=status.HTTP_404_NOT_FOUND)
    #     except sr.RequestError as e:
    #         return Response(f"Error en la solicitud al servicio de reconocimiento de voz: {e}", status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return Response("La tarea no tiene un archivo de audio adjunto", status=status.HTTP_404_NOT_FOUND)
