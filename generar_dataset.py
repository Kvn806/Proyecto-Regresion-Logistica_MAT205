import pandas as pd
import numpy as np

np.random.seed(42)

n = 200

promedio = np.random.randint(40,100,n)
asistencia = np.random.randint(30,100,n)
horas = np.random.randint(1,25,n)

abandona = []

for i in range(n):
    if promedio[i] < 60 and asistencia[i] < 60:
        abandona.append(1)
    else:
        abandona.append(0)

df = pd.DataFrame({
    "Promedio": promedio,
    "Asistencia": asistencia,
    "Horas_Estudio": horas,
    "Abandona": abandona
})

df.to_csv("dataset.csv", index=False)

print("Dataset creado correctamente")