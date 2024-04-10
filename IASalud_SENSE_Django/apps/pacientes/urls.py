from rest_framework import routers
from .api import PacienteViewSet

router = routers.DefaultRouter()

router.register('api/pacientes', PacienteViewSet, 'pacientes')

urlpatterns = router.urls