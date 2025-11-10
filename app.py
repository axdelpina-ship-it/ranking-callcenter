import streamlit as st
import pandas as pd

# Título de la app
st.title("Ranking de Satisfacción Semanal - Call Center")

# Cargar datos
df = pd.read_csv("puntajes.csv")

# Ordenar por puntos descendente
df = df.sort_values(by="Puntos", ascending=False)

# Mostrar tabla
st.subheader("Tabla de puntuaciones")
st.table(df)

# Mostrar gráfico de barras
st.subheader("Visualización de la carrera")
st.bar_chart(df.set_index("Nombre")["Puntos"])
