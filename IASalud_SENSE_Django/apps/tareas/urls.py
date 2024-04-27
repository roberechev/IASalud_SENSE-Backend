from rest_framework import routers
from .api import TareaViewSet
from rest_framework import routers
from .views import transcripcion_audio_texto
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register('api/tareas', TareaViewSet, 'tareas')

urlpatterns = router.urls

urlpatterns += [
    path('api/tareas/<int:tarea_id>/transcripcion_audio/', transcripcion_audio_texto, name='transcripcion_audio_texto'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


