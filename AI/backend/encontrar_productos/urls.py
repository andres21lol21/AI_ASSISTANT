from django.urls import path
from .views import generate_ad

urlpatterns = [
    path('api/generate_ad/', generate_ad, name='generate_ad'),
    
]

