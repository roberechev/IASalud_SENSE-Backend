from rest_framework import routers
from .api import PacienteViewSet
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import delete_paciente

router = routers.DefaultRouter()

router.register('api/pacientes', PacienteViewSet, 'pacientes')

urlpatterns = router.urls

urlpatterns += [
    path('api/pacientes/<int:paciente_id>/delete_paciente/', delete_paciente, name='delete_paciente')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)