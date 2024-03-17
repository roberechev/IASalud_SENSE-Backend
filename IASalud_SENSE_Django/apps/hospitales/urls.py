from rest_framework import routers
from .api import HospitalViewSet

router = routers.DefaultRouter()

router.register('api/hospitales', HospitalViewSet, 'hospitales')

urlpatterns = router.urls