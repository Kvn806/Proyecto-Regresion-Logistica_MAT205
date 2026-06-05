import pandas as pd

from sklearn.linear_model import LogisticRegression

import joblib

# Cargar dataset
df = pd.read_csv("dataset.csv")

# Variables de entrada
X = df[
    [
        "Promedio",
        "Asistencia",
        "Horas_Estudio"
    ]
]

# Variable objetivo
y = df["Abandona"]

# Crear modelo
modelo = LogisticRegression()

# Entrenar modelo
modelo.fit(X, y)

# Guardar modelo entrenado
joblib.dump(
    modelo,
    "modelo.pkl"
)

print("Modelo entrenado correctamente")