from rest_framework import routers
from .api import RegistroViewSet
# from .views import add_sensor_to_box, add_paciente_to_box, add_tarea_to_box, upload_audio_to_box
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register('api/registros', RegistroViewSet, 'registros')

urlpatterns = router.urls