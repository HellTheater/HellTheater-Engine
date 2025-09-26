import os
import replicate

class VideoGenerator:
    def generate(self, prompt, model_name="minimax/video-01"):
        # Diccionario de modelos disponibles en Replicate
        models = {
            "luma-reframe": "luma-ai/reframe-video",
            "minimax-video": "minimax-video-01",
            "google-imagen-4-video": "google/imagen-4" # Asumiendo que también puede generar videos
        }

        # Selecciona el modelo, o usa uno por defecto
        version = models.get(model_name, "minimax-video")

        try:
            # Replicate usa un sistema asíncrono, por lo que llamamos a la API
            # y esperamos a que complete la generación del video
            output = replicate.run(
                version,
                input={"prompt": prompt} # Aquí le pasamos el prompt
            )
            # El output será una lista o un objeto que contiene la URL del video
            if output and len(output) > 0:
                return output[0]  # Retorna la primera URL del video
            else:
                return "Error: No se recibió ninguna salida del modelo."
        except replicate.exceptions.ReplicateError as e:
            return f"Error de Replicate: {e}"
        except Exception as e:
            return f"Error inesperado: {e}"