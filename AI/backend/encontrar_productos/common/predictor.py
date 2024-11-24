import pandas as pd
import joblib
import os
from django.http import JsonResponse

def obtener_scores_de_categorias():
    # Ruta base del proyecto
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Ruta al archivo del modelo
    model_path = os.path.join(base_dir, '../../data/models/multi_category_model.pkl')

    # Cargar el modelo
    model = joblib.load(model_path)

    # Ruta al archivo trends_data.csv
    data_path = os.path.join(base_dir, '../../data/raw/trends_data.csv')

    # Cargar nuevos datos para predecir desde el archivo trends_data.csv
    nuevos_datos = pd.read_csv(data_path)

    # Filtrar solo las columnas relevantes
    nuevos_datos = nuevos_datos[['ropa', 'alimentos', 'electrodomesticos', 'muebles', 'libros', 'juguetes', 'automoviles', 'belleza', 'deportes', 'hogar']]

    # Realiza la predicción y convierte el resultado a una lista
    predicciones = model.predict(nuevos_datos).tolist()  # Convertimos a lista para JSON

    # Crea una lista de diccionarios con las categorías y sus scores promedios
    categorias = ['ropa', 'alimentos', 'electrodomesticos', 'muebles', 'libros', 'juguetes', 'automoviles', 'belleza', 'deportes', 'hogar']
    scores = [{"categoria": categorias[i], "score": sum(predicciones[i]) / len(predicciones[i])} for i in range(len(categorias))]

    return scores
