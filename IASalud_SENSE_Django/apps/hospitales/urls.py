from rest_framework import routers
from .api import HospitalViewSet
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from .views import add_box_to_hospital, add_paciente_to_hospital, get_device_info, devolver_dispositivos

router = routers.DefaultRouter()

router.register('api/hospitales', HospitalViewSet, 'hospitales')

urlpatterns = router.urls


urlpatterns += [
    path('api/hospitales/<int:hospital_id>/add_box/', add_box_to_hospital, name='add_box_to_hospital'),
    path('api/hospitales/<int:hospital_id>/add_paciente/', add_paciente_to_hospital, name='add_paciente_to_hospital'),
    # path('api/hospitales/thingsboard', get_device_info, name='get_device_info')
    path('api/hospitales/obtenerDispositivos', devolver_dispositivos, name='devolver_dispositivos')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
