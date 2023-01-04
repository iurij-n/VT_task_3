from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DeviceViewSet

router = DefaultRouter()

router.register('devices', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
