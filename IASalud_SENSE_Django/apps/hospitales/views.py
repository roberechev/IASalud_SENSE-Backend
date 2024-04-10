from django.shortcuts import render
from .models import Box, Paciente, Hospital
from rest_framework.response import Response
from rest_framework import status

import logging
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
# Importing the API exception
from tb_rest_client.rest import ApiException

from django.http import JsonResponse
from rest_framework.decorators import api_view



@api_view(['POST'])
def add_box_to_hospital(request, hospital_id):
    try:
        hospital = Hospital.objects.get(pk=hospital_id)
    except Box.DoesNotExist:
        return Response({"error": "Hospital does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    id_box = request.data.get('id_box')  # Obtener el ID del sensor del cuerpo de la solicitud
    
    try:
        box = Box.objects.get(pk=id_box)  # Obtener el sensor correspondiente al ID proporcionado
        hospital.boxes.add(box)  # Agregar el sensor al box
        hospital.save()
        return Response({"message": "Box added to hospital successfully"}, status=status.HTTP_201_CREATED)
    except Box.DoesNotExist:
        return Response({"error": "Box does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'El hospital ya tiene asignada ese Box.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_paciente_to_hospital(request, hospital_id):
    try:
        hospital = Hospital.objects.get(pk=hospital_id)
    except Box.DoesNotExist:
        return Response({"error": "Hospital does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    id_paciente = request.data.get('id_paciente')  # Obtener el ID del sensor del cuerpo de la solicitud
    
    try:
        paciente = Paciente.objects.get(pk=id_paciente)  # Obtener el sensor correspondiente al ID proporcionado
        hospital.pacientes.add(paciente)  # Agregar el sensor al box
        hospital.save()
        return Response({"message": "Paciente added to hospital successfully"}, status=status.HTTP_201_CREATED)
    except Paciente.DoesNotExist:
        return Response({"error": "Paciente does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'El hospital ya tiene asignada ese Paciente.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def devolver_dispositivos(request):
    with RestClientCE(base_url=url) as rest_client:
        try:
            rest_client.login(username=username, password=password)
            found_device = rest_client.get_tenant_device_infos(page_size=20, page=0)
            print("------Found device by id lo que QUIERO: \n%r", found_device)
            dispositivos = {}
            for device_info in found_device.data:
                dispositivos[device_info.id.id] = device_info.name
            # Devolver el diccionario en la respuesta
            return Response({
                'dispositivosIds': dispositivos,
            })
        except ApiException as e:
            logging.exception(e)







import logging
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
# Importing the API exception
from tb_rest_client.rest import ApiException


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = "http://localhost:8080"
# Default Tenant Administrator credentials
username = "tenant@thingsboard.org"
password = "tenant"

#@csrf_exempt
@api_view(['GET'])
def get_device_info(request):
    if request.method == 'GET':
        try:
            print("-------------------------------------------------------ROBER pruebaDispositivosGestion-------------------------------------------------------")
            devolver_dispositivos()
            return JsonResponse({'message': 'Información del dispositivo obtenida correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def pruebaDispositivosGestion():
    # Creating the REST client object with context manager to get auto token refresh
    with RestClientCE(base_url=url) as rest_client:
        try:
            rest_client.login(username=username, password=password)
            # # creating a Device
            # default_device_profile_id = rest_client.get_default_device_profile_info().id
            # print("default_device_profile_id: ", default_device_profile_id)
            # device = Device(name="PruebaPython2",
            #                 device_profile_id=default_device_profile_id)
            # device = rest_client.save_device(device)
            # logging.info(" Device was created:\n%r\n", device)
            
           # Especificar el tamaño de página y la página (por ejemplo, 10 dispositivos por página)
            # page_size = 10
            # page = 1
            
            # # Obtener una lista de dispositivos
            # devices = rest_client.get_tenant_devices(page_size=page_size, page=page)
            
            # # Imprimir los datos de cada dispositivo
            # for d in devices:
            #     print("Datos del dispositivo:")
            #     print(d)
            # '6f9c11c0-deda-11ee-82da-4d2b8f4eb4f7'
        
            # find device by device id
            found_device = rest_client.get_device_by_id(DeviceId('6f9c11c0-deda-11ee-82da-4d2b8f4eb4f7', 'DEVICE'))
            print("------Found device by id lo que QUIERO: \n%r", found_device)

            # save device shared attributes
            # rest_client.save_device_attributes(DeviceId(device.id, 'DEVICE'), 'SERVER_SCOPE', {'targetTemperature': 27})

            # # Get device shared attributes
            res = rest_client.get_attributes_by_scope(EntityId('6f9c11c0-deda-11ee-82da-4d2b8f4eb4f7', 'DEVICE'), 'SERVER_SCOPE', 'targetTemperature')# quitar 'targetTemperature' para obtener todos los datos del device
            print("----------------Datos Rober: \n%r", res)

            # delete the device
            # rest_client.delete_device(DeviceId(device.id, 'DEVICE'))
        except ApiException as e:
            logging.exception(e)

















# def dispositivoPrueba():
#     # Creating the REST client object with context manager to get auto token refresh
#     with RestClientCE(base_url=url) as rest_client:
#         try:
#             rest_client.login(username=username, password=password)
#             res = rest_client.get_tenant_device_infos(page_size=10, page=0)
#             logging.info("Device info:\n%r", res)
#             # Iterar sobre los datos y acceder a la información de cada dispositivo
            
#             for device_info in res.data:
#                 name = device_info.name
#                 device_type = device_info.type   
#                 id_device = device_info.id.id
                
#                 #esto saca como hacer post de mis devices:
#                 telemetry_data = rest_client.get_device_publish_telemetry_commands(id_device)
#                 logging.info("Telemetría----::\n %r", telemetry_data)
                
#                 logging.info("Nombre del dispositivo: %s, Tipo: %s, ID: %s", name, device_type, id)
                
#             dash = rest_client.get_user_dashboards_info()
#             logging.info("ROBER: %r", dash)
#         except ApiException as e:
#             logging.exception(e)        
            


# def pppABC():
#     # Configura la URL base de la API REST de ThingsBoard
#     thingsboard_url = 'http://localhost:8080'

#     # Default Tenant Administrator credentials
#     username = "tenant@thingsboard.org"
#     password = "tenant"

#     # Realiza la solicitud de inicio de sesión para obtener el token de acceso
#     login_url = f'{thingsboard_url}/api/auth/login'
#     login_data = {'username': username, 'password': password}
#     response = requests.post(login_url, json=login_data)

#     # Verifica si la solicitud fue exitosa
#     if response.status_code == 200:
#         # Extrae el token de acceso del cuerpo de la respuesta
#         token = response.json()['token']

#         # Configura los encabezados de autorización para futuras solicitudes
#         headers = {'Authorization': f'Bearer {token}'}

#         # Ejemplo de cómo obtener la lista de dispositivos
#         devices_url = f'{thingsboard_url}/api/tenant/devices'
#         devices_response = requests.get(devices_url, headers=headers)

#         print("ROBER ", devices_response)
#         # Verifica si la solicitud de dispositivos fue exitosa
#         if devices_response.status_code == 200:
#             devices_data = devices_response.json()
#             # Itera sobre los dispositivos y muestra sus valores
#             for device in devices_data:
#                 print(f"ID: {device['id']}, Nombre: {device['name']}")
#                 # Utiliza el UUID del dispositivo en lugar de "devices" en la URL de telemetría
#                 telemetry_url = f'{thingsboard_url}/api/plugins/telemetry/{device["id"]}/values/timeseries?keys=temperature'
#                 telemetry_response = requests.get(telemetry_url, headers=headers)
#                 if telemetry_response.status_code == 200:
#                     telemetry_data = telemetry_response.json()
#                     print("Telemetría:", telemetry_data)
#                 else:
#                     print("Error al obtener telemetría:", telemetry_response.text)
#         else:
#             print("Error al obtener la lista de dispositivos:", devices_response.text)
#     else:
#         print("Error al iniciar sesión:", response.text)
        
# import sys, time, json, random,requests
# import paho.mqtt.client as mqtt
        
# def mqttPrueba():
#     THINGSBOARD_HOST = 'http://localhost:8080'
#     ACCESS_TOKEN = 'T2_TEST_TOKEN'
    
#     sensor_data = {'temperature': 25, 'humidity': 65}
    
#     client = mqtt.Client()
#     client.username_pw_set(ACCESS_TOKEN)
#     client.connect(THINGSBOARD_HOST, 1883)
#     client.loop_start()

#     try:
#         temperature = sensor_data['temperature'] + random.uniform(-3, 3)
#         humidity = sensor_data['humidity'] + random.uniform(-3, 3)
#         sensor_data['temperature'] = temperature
#         sensor_data['humidity'] = humidity
        
#         client.publish('v1/devices/me/telemetry', json.dumps(sensor_data))
#         time.sleep(10)
            
#     except KeyboardInterrupt:
#         pass
#     client.loop_stop()
#     client.disconnect()



# # no puedes obtener todos los datos en una sola llamada. Necesita dos llamadas: (GET /api/tenant/devices) y (GET /api/plugins/telemetry/DEVICE/{entityId}/values/attributes/SERVER_SCOPE) para él