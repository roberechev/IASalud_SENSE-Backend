from rest_framework import routers
from .api import SensorViewSet
from .views import add_registro_to_sensor
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register('api/sensores', SensorViewSet, 'sensores')

urlpatterns = router.urls

urlpatterns += [
    path('api/sensores/<int:sensor_id>/add_registro/', add_registro_to_sensor, name='add_registro_to_sensor')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)