# assistant/serializers.py
from rest_framework import serializers
from .models import Product  # Importamos nuestro modelo Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']
