import pandas as pd
import numpy as np
from datasets import load_dataset
#Para descargar vamos a usar la librería datasets descargada previamente tal como lo propone el proyecto,
#debemos ejecutar el siguiente framento de código:

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
# Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.

df = pd.DataFrame(data)

#Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron 
#(is_dead=1) y otro con el complemento.

df_fallecidos = df[df["is_dead"] == 1]
df_no_fallecidos = df[df["is_dead"] == 0]

print(df_fallecidos)
print(df_no_fallecidos)

#Calcular los promedios de las edades de cada dataset e imprimir.
promedio_edades = df['age'].mean()
print(f"El promedio de edad de las personas participantes en el estudio es: {promedio_edades:.2f} años.")


