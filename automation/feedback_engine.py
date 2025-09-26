import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class FeedbackEngine:
    """
    Agente de retroalimentación para la auto-reingeniería del sistema.
    Analiza métricas de éxito y recomienda ajustes.
    """
    def __init__(self):
        self.metrics_history = pd.DataFrame(columns=[
            'timestamp', 'tasa_interaccion', 'resonancia_semantica', 
            'tiempo_respuesta', 'nivel_ejecutado', 'idea_original', 'recomendacion'
        ])

    def record_metrics(self, data):
        """
        Registra las métricas de la última operación en el historial.
        """
        new_row = {
            'timestamp': datetime.now(),
            'tasa_interaccion': data.get('interaccion_likes_rt_avg', 0),
            'resonancia_semantica': data.get('repeticion_terminos_clave', 0),
            'tiempo_respuesta': data.get('tiempo_respuesta_nodo', 0),
            'nivel_ejecutado': data.get('nivel_de_operacion', 0),
            'idea_original': data.get('idea_principal', ''),
            'recomendacion': 'N/A'
        }
        self.metrics_history = pd.concat([self.metrics_history, pd.DataFrame([new_row])], ignore_index=True)

    def analyze_and_recommend(self, last_operation_data):
        """
        Analiza los resultados de la última operación y genera una recomendación.
        """
        self.record_metrics(last_operation_data)
        
        # Lógica de análisis y decisión
        interaccion = last_operation_data.get('interaccion_likes_rt_avg', 0)
        resonancia = last_operation_data.get('repeticion_terminos_clave', 0)
        tiempo_respuesta = last_operation_data.get('tiempo_respuesta_nodo', 0)
        
        # Umbrales para la decisión
        umbral_exito_interaccion = 0.5
        umbral_exito_resonancia = 0.3
        umbral_fracaso_tiempo = 3600  # Más de una hora de respuesta

        recomendacion = {
            "estado": "análisis completado",
            "ajuste_sugerido": "mantener estrategia",
            "motivo": "Los resultados están dentro de los parámetros esperados."
        }

        # Lógica para escalar si el éxito es alto
        if interaccion > umbral_exito_interaccion and resonancia > umbral_exito_resonancia:
            recomendacion['ajuste_sugerido'] = "escalar nivel de intervención"
            recomendacion['motivo'] = "La narrativa tuvo alta resonancia e interacción. Se recomienda reforzar con una operación de nivel superior."
        
        # Lógica para reajustar si el resultado es bajo
        elif interaccion < 0.1 or resonancia < 0.1 or tiempo_respuesta > umbral_fracaso_tiempo:
            recomendacion['ajuste_sugerido'] = "re-evaluar narrativa"
            recomendacion['motivo'] = "La operación no logró el impacto esperado. Se recomienda cambiar la narrativa o el perfil psicográfico objetivo."
        
        # Lógica para iterar si el resultado es neutro
        else:
            recomendacion['ajuste_sugerido'] = "iterar con ajustes menores"
            recomendacion['motivo'] = "Resultados prometedores, pero no óptimos. Se recomienda ajustar el tono emocional o la temporalidad."

        self.metrics_history.loc[self.metrics_history.index[-1], 'recomendacion'] = recomendacion['ajuste_sugerido']

        return recomendacion

    def get_full_report(self):
        """
        Devuelve el historial completo de operaciones para auditoría.
        """
        return self.metrics_history.to_dict('records')
