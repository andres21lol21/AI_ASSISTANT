# assistant/views.py
from rest_framework import generics
from .models import Product  # Importamos nuestro modelo Product
from .serializers import ProductSerializer  # Importamos nuestro serializador

class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()  # Queremos todos los productos
    serializer_class = ProductSerializer  # Usamos nuestro serializador para los datos

# assistant/views.py
from django.shortcuts import render
from .models import Product

# Función simulada para obtener productos de alta demanda
def get_high_demand_products():
    high_demand_products = [
        {'name': 'Producto Popular 1', 'description': 'Descripción del Producto Popular 1', 'price': 29.99},
        {'name': 'Producto Popular 2', 'description': 'Descripción del Producto Popular 2', 'price': 39.99},
        {'name': 'Producto Popular 3', 'description': 'Descripción del Producto Popular 3', 'price': 19.99},
    ]
    return high_demand_products

# Función simulada para generar anuncios publicitarios
def generate_advertisement(product):
    return f"¡Compra {product['name']} por solo ${product['price']}! {product['description']}"

# Vista para listar productos
def product_list(request):
    products = Product.objects.all()  # Obtener todos los productos de la base de datos
    high_demand_products = get_high_demand_products()  # Obtener productos de alta demanda
    advertisements = [generate_advertisement(product) for product in high_demand_products]  # Generar anuncios
    return render(request, 'assistant/product_list.html', {
        'products': products,
        'high_demand_products': high_demand_products,
        'advertisements': advertisements
    })

# Vista para el chatbot
def chatbot(request):
    return render(request, 'assistant/chatbot.html')

