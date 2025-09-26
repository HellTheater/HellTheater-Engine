# ...existing code...
import streamlit as st
import os
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="HellTheatre OS", layout="wide")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {background-color: #0f0f0f; color: #ffffff;}
    table.dataframe td, table.dataframe th {color: #ffffff;}
    </style>
""", unsafe_allow_html=True)

# autenticación simple
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔐 HellTheatre OS - Acceso restringido")
    pwd = st.text_input("Clave de acceso:", type="password")
    if st.button("Ingresar"):
        if pwd == os.getenv("HT_PASSWORD"):
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("Clave incorrecta")
    st.stop()

# DB
conn = sqlite3.connect('helltheatre_real.db', check_same_thread=False)
cursor = conn.cursor()

st.title("🎭 HellTheatre OS - Dashboard Estratégico")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Métricas en Tiempo Real",
    "📁 Historial de Estrategias",
    "🚀 Estrategias en Ejecución",
    "✅ Aprobación y Control",
    "📈 Visualización de Datos",
    "💬 Chat con el Sistema"
])

with tab1:
    st.subheader("📊 Métricas en Tiempo Real")
    try:
        cursor.execute("SELECT COUNT(*) FROM sesiones")
        total_sessions = cursor.fetchone()[0]
        cursor.execute("SELECT fecha FROM sesiones ORDER BY fecha DESC LIMIT 1")
        last_run = cursor.fetchone()
        st.metric("Sesiones ejecutadas", total_sessions)
        st.metric("Última ejecución", last_run[0] if last_run else "N/A")
    except Exception as e:
        st.warning(f"No existe tabla 'sesiones'. {e}")

    try:
        cursor.execute("SELECT COUNT(*) FROM estrategias")
        total = cursor.fetchone()[0]
        st.metric("Estrategias registradas", total)
    except:
        st.warning("No existe tabla 'estrategias'.")

with tab2:
    st.subheader("📁 Historial de Estrategias")
    try:
        cursor.execute("SELECT id, nombre, nivel, fecha, resultado FROM estrategias ORDER BY fecha DESC LIMIT 50")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=["ID","Nombre","Nivel","Fecha","Resultado"])
        st.dataframe(df)
    except Exception as e:
        st.info(f"No hay estrategias registradas. {e}")

with tab3:
    st.subheader("🚀 Estrategias en Ejecución")
    try:
        cursor.execute("SELECT nombre, nivel, fecha, resultado FROM estrategias ORDER BY fecha DESC LIMIT 1")
        cur = cursor.fetchone()
        if cur:
            st.write(f"🕒 Ejecutada: {cur[2]}")
            st.write(f"🎯 Estrategia: {cur[0]}")
            st.write(f"🔢 Nivel: {cur[1]}")
            st.write(f"📋 Resultado: {cur[3]}")
        else:
            st.info("No hay ejecución activa.")
    except Exception as e:
        st.warning(f"Error lectura: {e}")

with tab4:
    st.subheader("✅ Aprobación y Control Manual")
    action = st.radio("Acción:", ["Aprobar estrategia","Rechazar estrategia","Detener ejecución","Cambiar nivel"])
    if action == "Cambiar nivel":
        lvl = st.selectbox("Nuevo nivel:", [1,2,3])
        if st.button("Aplicar"):
            st.success(f"Nivel cambiado a {lvl}")
    elif st.button("Ejecutar acción"):
        st.success(f"Acción '{action}' ejecutada")

with tab5:
    st.subheader("📈 Visualización de Datos")
    try:
        cursor.execute("SELECT fuente, consulta, fecha, sentimiento, sentimiento_score FROM scraping_resultados ORDER BY fecha DESC LIMIT 200")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=["Fuente","Consulta","Fecha","Sentimiento","Score"])
        if not df.empty:
            st.dataframe(df)
            trend_count = df.groupby("Fuente").size().reset_index(name="Cantidad")
            fig1 = px.bar(trend_count, x="Fuente", y="Cantidad", title="Volumen por Fuente")
            st.plotly_chart(fig1, use_container_width=True)

            sentiment_avg = df.groupby("Fuente")["Score"].mean().reset_index()
            fig2 = px.bar(sentiment_avg, x="Fuente", y="Score", title="Sentimiento promedio por Fuente")
            st.plotly_chart(fig2, use_container_width=True)

            heat = df.pivot_table(index="Fuente", columns="Sentimiento", values="Score", aggfunc="mean").fillna(0)
            fig3 = go.Figure(data=go.Heatmap(z=heat.values, x=heat.columns, y=heat.index, colorscale='turquoise'))
            fig3.update_layout(title="Termografía de Sentimiento")
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("No hay datos de scraping.")
    except Exception as e:
        st.info(f"No hay datos: {e}")

with tab6:
    st.subheader("💬 Chat con el Sistema")
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    col1, col2 = st.columns([4,1])
    with col1:
        user = st.text_input("Pregunta al sistema:")
    with col2:
        if st.button("Enviar"):
            resp = "Respuesta simulada: solicita análisis o ejecución."
            st.session_state.chat_history.append(("Usuario", user))
            st.session_state.chat_history.append(("Sistema", resp))
    for who, msg in st.session_state.chat_history:
        st.write(f"**{who}:** {msg}")