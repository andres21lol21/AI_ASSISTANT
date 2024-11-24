from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
import openai
from django.conf import settings

class AIResponseView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST.get("message", "")
        if data:
            try:
                # Aquí agregamos la lógica para enviar la solicitud a OpenAI
                response = openai.Completion.create(
                    model="text-davinci-003",  # Ejemplo de modelo
                    prompt=data,
                    max_tokens=150
                )
                reply = response.choices[0].text.strip()
                return JsonResponse({"response": reply})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
        return JsonResponse({"error": "No message provided"}, status=400)