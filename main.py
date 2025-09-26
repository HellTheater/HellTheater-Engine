import os
from dotenv import load_dotenv

# --- Módulos Principales ---
from automation.feedback_engine import FeedbackEngine
from influence.strategy_engine import StrategyEngine
from automation.calendar_scheduler import CalendarScheduler
from automation.email_notifier import send_email

# --- Motores de Operación ---
from scraping_engines.twitter_scraper import TwitterScraper
from scraping_engines.reddit_scraper import RedditScraper
from ai_engines.emotion_analyzer import EmotionAnalyzer
from ai_engines.text_generator import TextGenerator
from ai_engines.trend_predictor import TrendPredictor
from ai_engines.impact_simulator import ImpactSimulator  # Nuevo agente


# ==========================================================
# FASE 1: PROVISIONAMIENTO E INICIALIZACIÓN DE AGENTES
# ==========================================================
# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Inicialización de todos los agentes operativos
twitter = TwitterScraper()
reddit = RedditScraper()
emotion = EmotionAnalyzer()
generator = TextGenerator()
scheduler = CalendarScheduler()
feedback_engine = FeedbackEngine()
trend_predictor = TrendPredictor()
impact_simulator = ImpactSimulator() # Inicializa el simulador


# ==========================================================
# FASE 2: PLANIFICACIÓN Y EJECUCIÓN DE ESTRATEGIA
# ==========================================================
# Definición del contexto y el objetivo de la operación
objective = "monetizar cuenta nueva"
keywords = "minimalismo digital"
level = 2
platform = "twitter"
idea = "quiero una banana"

# Despliegue de agentes de scraping y análisis de datos
twitter_data = twitter.scrape(keywords, limit=50)
reddit_data = reddit.scrape("technology", limit=30)
sample_text = twitter_data[0]["content"] if twitter_data else "sin datos"
emotion_detected = emotion.analyze(sample_text)

# Despliegue de agente de generación de contenido
prompt = f"Genera un hilo de Twitter sobre {keywords} con tono de {emotion_detected}"
content = generator.generate(prompt, max_length=150)

# ==========================================================
# FASE 3: SIMULACIÓN DE IMPACTO (PRE-EJECUCIÓN)
# ==========================================================
st.write("Iniciando simulación de impacto...")
simulation_report = impact_simulator.simulate_diffusion(idea)
st.json(simulation_report)

# ==========================================================
# FASE 4: CALENDARIZACIÓN Y EJECUCIÓN
# ==========================================================
optimal_times = ["10:00", "19:00", "22:00"]
calendar = scheduler.schedule(optimal_times)

# Ejecución de la estrategia según el nivel definido
context = {
    "objective": objective,
    "keywords": keywords,
    "emotion": emotion_detected,
    "content": content,
    "calendar": calendar,
    "twitter_data": twitter_data,
    "reddit_data": reddit_data
}
engine = StrategyEngine(level)
strategy_result = engine.execute(context)


# ==========================================================
# FASE 5: ANÁLISIS DE RETROALIMENTACIÓN Y RE-INGENIERÍA
# ==========================================================
# Datos de éxito simulados para el análisis de retroalimentación
mock_success_data = {
    "interaccion_likes_rt_avg": 0.75,
    "repeticion_terminos_clave": 0.45,
    "tiempo_respuesta_nodo": 30,
    "nivel_de_operacion": level,
    "idea_principal": keywords
}
feedback_report = feedback_engine.analyze_and_recommend(mock_success_data)


# ==========================================================
# FASE 6: REPORTE DE INTELIGENCIA Y NOTIFICACIÓN AL DIRECTOR
# ==========================================================
subject = f"Estrategia HellTheatre OS - Nivel {level}"
body = f"""
[REPORTE DE OPERACIÓN]
Objetivo: {objective}
Tendencia: {keywords}
Emoción dominante: {emotion_detected}
Contenido generado: {content}
Resultado de la estrategia: {strategy_result}
---
[ANÁLISIS DE SIMULACIÓN]
Estado de la simulación: {simulation_report['estado']}
Impacto promedio: {simulation_report['impacto_total_promedio']}
---
[ANÁLISIS DE RETROALIMENTACIÓN]
Estado: {feedback_report['estado']}
Recomendación: {feedback_report['ajuste_sugerido']}
Motivo: {feedback_report['motivo']}
---
[INFORME AUDITOR COMPLETO]
{feedback_engine.get_full_report()}
"""
director_email = os.getenv("DIRECTOR_EMAIL", "director@helltheatre.local")
send_email(director_email, subject, body)

# Confirmación final de la operación
print("✅ Estrategia ejecutada, simulada, analizada por retroalimentación y notificada al director.")
