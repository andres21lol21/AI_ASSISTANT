from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import openai
import json
from decouple import config

# Cargar clave de API desde .env
OPENAI_API_KEY = config('OPENAI_API_KEY')

# Configura correctamente tu clave de API
# openai.api_key = "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"

@csrf_exempt  # Este decorador desactiva la protección CSRF para esta vista
def generate_ad(request):
    if request.method == "POST":
        try:
            # Parsear el cuerpo de la solicitud como JSON
            data = json.loads(request.body)
            product_name = data.get("product_name", "Producto Genérico")
            target_audience = data.get("target_audience", "audiencia general")
            tone = data.get("tone", "neutro")

            # Crear el prompt para el texto del anuncio
            ad_prompt = f"""
            Eres un experto en marketing digital. Crea un anuncio breve y persuasivo para redes sociales:
            - Producto: {product_name}
            - Público objetivo: {target_audience}
            - Tono: {tone}
            """

            # Solicitud a OpenAI para generar el texto del anuncio
            ad_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": ad_prompt}],
                max_tokens=150,  # Número moderado de tokens
                temperature=0.7,  # Controlar la creatividad
                top_p=1.0  # Limitar la aleatoriedad
            )

            # Extraer el texto del anuncio
            ad_text = ad_response['choices'][0]['message']['content']

            # Crear el prompt para la idea de la imagen
            image_prompt = f"""
            Eres un creativo experto en marketing visual. Imagina una imagen que acompañe este anuncio:
            - Producto: {product_name}
            - Público objetivo: {target_audience}
            - Tono: {tone}
            """

            # Solicitud a OpenAI para generar la idea de la imagen
            image_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": image_prompt}],
                max_tokens=150,  # Número moderado de tokens
                temperature=0.7,  # Controlar la creatividad
                top_p=1.0  # Limitar la aleatoriedad
            )

            # Extraer la idea de la imagen
            image_idea = image_response['choices'][0]['message']['content']

            # Respuesta JSON final
            return JsonResponse({"ad_text": ad_text, "image_idea": image_idea})

        except openai.OpenAIError as e:
            return JsonResponse({"error": f"OpenAI API Error: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"Error inesperado: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)
