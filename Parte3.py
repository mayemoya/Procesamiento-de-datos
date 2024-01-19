import pandas as pd
import numpy as np
from datasets import load_dataset
#Para descargar vamos a usar la librería datasets descargada previamente tal como lo propone el proyecto,
#debemos ejecutar el siguiente framento de código:

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
# Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.

df = pd.DataFrame(data)

#Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan 
#colúmnas numéricas en formato de cadena).

# Verificar los tipos de datos actuales
print("Tipos de datos actuales:")
print(df.dtypes)

#Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas).

# Filtrar por hombres fumadores

df_hombres_fumadores = df[(df['is_male'] == True) & (df['is_smoker'] == True)]

# Filtrar por mujeres fumadoras 
df_mujeres_fumadoras = df[(df['is_male'] == False) & (df['is_smoker'] == True)]

# Obtener la cantidad de hombres y mujeres fumadores
cantidad_hombres_fumadores = len(df_hombres_fumadores)
cantidad_mujeres_fumadoras = len(df_mujeres_fumadoras)

# Mostrar los resultados
print("Cantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)


