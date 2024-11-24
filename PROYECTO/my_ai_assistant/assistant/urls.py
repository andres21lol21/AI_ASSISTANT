

# assistant/urls.py
from django.urls import path
from . import views
from .views import ProductListAPIView , TrendingProductListAPIView

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('api/products/', ProductListAPIView.as_view(), name='product-list-api'),
   
]
