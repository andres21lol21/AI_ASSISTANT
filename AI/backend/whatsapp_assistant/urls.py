from django.urls import path
from .views import AIResponseView
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Assistant API is working"})

urlpatterns = [
    path('', home, name='assistant-home'),  # Ruta para responder en assistant/
    path('ai-response/', AIResponseView.as_view(), name='ai_response')
]
