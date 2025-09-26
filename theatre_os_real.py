import streamlit as st
import numpy as np
import base64
import os
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Módulos Principales ---
from automation.feedback_engine import FeedbackEngine
from influence.strategy_engine import StrategyEngine
from automation.calendar_scheduler import CalendarScheduler
from automation.email_notifier import send_email

# --- Motores de Operación ---
from scraping_engines.twitter_scraper import TwitterScraper
from scraping_engines.reddit_scraper import RedditScraper
from scraping_engines.tiktok_scraper import TiktokScraper
from scraping_engines.instagram_scraper import InstagramScraper
from scraping_engines.news_scraper import NewsScraper

from ai_engines.emotion_analyzer import EmotionAnalyzer
from ai_engines.text_generator import TextGenerator
from ai_engines.trend_predictor import TrendPredictor
from ai_engines.impact_simulator import ImpactSimulator

# CONFIGURACIÓN
st.set_page_config(page_title="HellTheatre OS", layout="wide")
load_dotenv()
PASSWORD = os.getenv("HT_PASSWORD")

# Inicializar agentes (lazy)
@st.cache_resource
def initialize_agents():
    return {
        "twitter": TwitterScraper(),
        "reddit": RedditScraper(),
        "tiktok": TiktokScraper(),
        "instagram": InstagramScraper(),
        "news": NewsScraper(),
        "emotion": EmotionAnalyzer(),
        "generator": TextGenerator(),
        "scheduler": CalendarScheduler(),
        "feedback": FeedbackEngine(),
        "predictor": TrendPredictor(),
        "simulator": ImpactSimulator()
    }

# Utilidades de assets
def get_base64_of_image(path):
    try:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Error: No se encontró la imagen: {path}")
        return None

def set_bg_image():
    b64 = get_base64_of_image("assets/bg.png")
    if b64:
        st.markdown(f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{b64}");
                background-size: cover;
                background-attachment: fixed;
                background-position: center;
                color: #B2D8D8;
                font-family: 'Courier New', monospace;
            }}
            .chat-block {{
                width: 20vw;
                min-width: 320px;
                max-width: 520px;
                margin: 40px auto;
                background: rgba(20,20,20,0.78);
                border-radius: 14px;
                padding: 18px;
                box-shadow: 0 6px 24px rgba(0,0,0,0.45);
            }}
            </style>
        """, unsafe_allow_html=True)

set_bg_image()

# Estado sesión
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Modo escucha
if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align:center;color:#00FFFF;'>Conecta con el Sistema</h1>", unsafe_allow_html=True)
    st.markdown('<div class="chat-block">', unsafe_allow_html=True)
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(msg)
    user_input = st.chat_input("Escribe tu comando o pregunta...")
    st.markdown('</div>', unsafe_allow_html=True)

    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        if PASSWORD and user_input.strip() == PASSWORD:
            st.session_state.authenticated = True
            st.session_state.chat_history.append(("assistant", "Clave verificada. Acceso autorizado."))
            st.rerun()
        else:
            st.session_state.chat_history.append(("assistant", "Analizando el contexto..."))
else:
    agents = initialize_agents()
    st.markdown("<h1 style='text-align:center;color:#00FFFF;'>HellTheatre OS - Centro de Mando</h1>", unsafe_allow_html=True)

    def load_icon(path):
        try:
            with open(f"assets/{path}", "rb") as f:
                return base64.b64encode(f.read()).decode("utf-8")
        except FileNotFoundError:
            return None

    cols = st.columns(4)
    icons = ["logo.png", "icon_dashboard.png", "icon_strategy.png", "icon_decision.png"]
    for c, icon in zip(cols, icons):
        b = load_icon(icon)
        if b:
            c.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{b}" width="96"/></div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 Ecosistema","📁 Estrategias","🧠 Proyecciones"])

    with tab1:
        st.subheader("Análisis del Ecosistema")
        # Llamadas reales a scraping (ejemplo)
        try:
            twitter_data = agents["twitter"].scrape("IA", limit=50)
            df_t = pd.DataFrame(twitter_data)
            if not df_t.empty:
                fig = px.bar(df_t.groupby(df_t['sentiment']).size().reset_index(name='count'),
                             x='sentiment', y='count', color='sentiment', title='Sentimiento en Twitter')
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.warning(f"No se pudo obtener datos Twitter: {e}")

    with tab2:
        st.subheader("Reporte de Operaciones")
        try:
            strategies_report = agents["feedback"].get_full_report()
            st.json(strategies_report)
        except Exception:
            st.info("Reporte de feedback no disponible.")

        # Impacto temporal (ejemplo desde simulator)
        try:
            impact = pd.DataFrame(agents["simulator"].simulate_history())
            if not impact.empty:
                fig_imp = px.line(impact, x='date', y='impact', title='Impacto Histórico')
                st.plotly_chart(fig_imp, use_container_width=True)
        except Exception:
            pass

    with tab3:
        st.subheader("Proyecciones")
        try:
            st.json(agents["predictor"].predict_optimal_moment())
        except Exception:
            st.info("Predictor no disponible.")

    # Chat operativo
    st.markdown('<div class="chat-block">', unsafe_allow_html=True)
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(msg)
    user_input = st.chat_input("Escribe tu comando al sistema...")
    st.markdown('</div>', unsafe_allow_html=True)
    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("assistant", f"Recibido: {user_input}"))