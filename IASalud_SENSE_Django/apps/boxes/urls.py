from rest_framework import routers
from .api import BoxViewSet
from .views import add_sensor_to_box, add_paciente_to_box, add_tarea_to_box, upload_audio_to_box, eliminar_sensor_of_box, delete_box
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register('api/boxes', BoxViewSet, 'boxes')

urlpatterns = router.urls

urlpatterns += [
    path('api/boxes/<int:box_id>/upload-audio/', upload_audio_to_box, name='upload_audio_to_box'),
    path('api/boxes/<int:box_id>/add_sensor/', add_sensor_to_box, name='add_sensor_to_box'),
    path('api/boxes/<int:box_id>/eliminar_sensor/', eliminar_sensor_of_box, name='eliminar_sensor_of_box'),
    path('api/boxes/<int:box_id>/add_paciente/', add_paciente_to_box, name='add_paciente_to_box'),
    path('api/boxes/<int:box_id>/add_tarea/', add_tarea_to_box, name='add_tarea_to_box'),
    path('api/boxes/<int:box_id>/delete_box/', delete_box, name='delete_box')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

