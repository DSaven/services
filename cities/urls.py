from rest_framework import routers
from .api import CityViewSet


router = routers.DefaultRouter()
router.register('api/v0/cities', CityViewSet, 'cities')

urlpatterns = router.urls
