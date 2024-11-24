# encontrar_productos/serializers.py

from rest_framework import serializers

class CategoriaSerializer(serializers.Serializer):
    categoria = serializers.CharField(max_length=255)
    puntaje = serializers.FloatField()
