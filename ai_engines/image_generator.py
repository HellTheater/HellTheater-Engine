import os
import requests

class ImageGenerator:
    def generate(self, prompt, model_name="google/imagen-4"):
        # Diccionario de modelos disponibles
        models = {
            "google-imagen-4": "google/imagen-4",
            "ideogram-v3-turbo": "ideogram-ai/ideogram-v3-turbo",
            "flux-kontext-pro": "black-forest-labs/flux-kontext-pro"
        }

        # Selecciona el modelo, o usa uno por defecto
        version = models.get(model_name, models["google-imagen-4"])

        url = "https://api.replicate.com/v1/predictions"
        headers = {
            "Authorization": f"Token {os.getenv('REPLICATE_API_TOKEN', '')}",
            "Content-Type": "application/json"
        }
        data = {
            "version": version,
            "input": {"prompt": prompt}
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get("output", "")
        else:
            return f"Error al generar imagen. Código: {response.status_code}"