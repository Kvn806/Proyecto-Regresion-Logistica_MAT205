import streamlit as st
import joblib
import matplotlib.pyplot as plt

# Cargar modelo entrenado
modelo = joblib.load("modelo.pkl")

# Título
st.title("Predicción de Abandono Estudiantil")

st.write(
    "Modifica los valores y observa cómo cambia la probabilidad de abandono."
)

# Sliders
promedio = st.slider(
    "Promedio",
    min_value=0,
    max_value=100,
    value=70
)

asistencia = st.slider(
    "Asistencia (%)",
    min_value=0,
    max_value=100,
    value=80
)

horas = st.slider(
    "Horas de Estudio por Semana",
    min_value=0,
    max_value=30,
    value=10
)

# Nuevo estudiante
nuevo = [[
    promedio,
    asistencia,
    horas
]]

# Probabilidad
probabilidad = modelo.predict_proba(nuevo)[0][1]

# Predicción
prediccion = modelo.predict(nuevo)[0]

st.subheader(
    f"Probabilidad de abandono: {probabilidad:.2%}"
)

# Barra de progreso
st.progress(
    int(probabilidad * 100)
)

# Resultado
if prediccion == 1:
    st.error("RIESGO DE ABANDONO")
else:
    st.success("NO ABANDONA")

# Gráfico
fig, ax = plt.subplots()

ax.bar(
    ["Probabilidad"],
    [probabilidad]
)

ax.set_ylim(0, 1)
ax.set_ylabel("Probabilidad")

st.pyplot(fig)