# backend/urls.py
from django.contrib import admin
from django.urls import path, include

from encontrar_productos.views import generate_ad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/generate_ad/', generate_ad, name='generate_ad'),
    # Otras rutas de tu API
]

