import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="🏁 Carrera de Satisfacción", layout="wide")

st.title("🏆 Carrera de Satisfacción Semanal - Call Center 🏁")

# Cargar datos
df = pd.read_csv("puntajes.csv")

# Ordenar por puntos descendente
df = df.sort_values(by="Puntos", ascending=False).reset_index(drop=True)

# Crear columna con emojis según posición
emojis = ['🥇', '🥈', '🥉'] + ['🏃']*(len(df)-3)
df['Posición'] = emojis

# Mostrar tabla con posición y puntuación
st.subheader("Tabla de Puntuaciones")
def estilo_posicion(row):
    if row.name == 0:
        return ['background-color: gold; font-weight:bold']*len(row)
    elif row.name == 1:
        return ['background-color: silver; font-weight:bold']*len(row)
    elif row.name == 2:
        return ['background-color: #cd7f32; font-weight:bold']*len(row)
    else:
        return ['']*len(row)

st.dataframe(df.style.apply(estilo_posicion, axis=1))

# Visualización tipo carrera con barras
st.subheader("🏁 Visualización de la carrera")
bar_data = df.set_index("Nombre")["Puntos"]
st.bar_chart(bar_data)

# Mostrar emojis tipo carrera al lado de la barra
st.subheader("🏃‍♂️ Avance de cada operador")
for i, row in df.iterrows():
    st.markdown(f"{row['Posición']} **{row['Nombre']}**: {row['Puntos']} puntos")
