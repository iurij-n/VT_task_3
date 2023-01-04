from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('devices_api/v1/', include('devices.urls')),
    path('admin/', admin.site.urls),
]
