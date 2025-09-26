import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class TrendPredictor:
    """
    Agente de predicción de tendencias para anticipar el comportamiento de las narrativas.
    Simula la proyección de series temporales para encontrar el momento óptimo.
    """
    def __init__(self):
        # Historial simulado de interacciones para la proyección
        self.historical_data = {
            "date": [datetime.now() - timedelta(days=d) for d in range(10, 0, -1)],
            "mentions": [np.random.randint(10, 50) for _ in range(10)]
        }
        self.df = pd.DataFrame(self.historical_data)

    def analyze_historical_data(self, new_data):
        """
        Incorpora nuevos datos de scraping para refinar la predicción.
        """
        if new_data:
            mentions = len(new_data)
            new_row = {"date": datetime.now(), "mentions": mentions}
            new_df = pd.DataFrame([new_row])
            self.df = pd.concat([self.df, new_df], ignore_index=True)

    def predict_optimal_moment(self):
        """
        Simula una proyección de serie temporal para encontrar el mejor momento para actuar.
        """
        # Una lógica simplificada para demostrar la funcionalidad
        # En una versión real, usaríamos modelos como Prophet o ARIMA
        last_mentions = self.df['mentions'].iloc[-3:]
        
        # Si la tendencia es creciente, la oportunidad es inminente
        is_trending_up = all(last_mentions.diff().dropna() > 0)
        
        if is_trending_up:
            optimal_moment = datetime.now() + timedelta(hours=3)
            return {
                "estado": "tendencia al alza",
                "momento_optimo": optimal_moment.isoformat(),
                "motivacion": "La narrativa está en una fase de crecimiento acelerado. Se recomienda una inserción inmediata para maximizar el impacto."
            }
        else:
            return {
                "estado": "tendencia estable o en declive",
                "momento_optimo": "N/A",
                "motivacion": "La narrativa no muestra una tendencia clara. Se recomienda continuar la observación o buscar un punto de ruptura."
            }