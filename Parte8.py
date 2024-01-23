#Usando el mismo DataFrame, realiza una gráfica usando subplots, que contenga gráficas de torta que represente las 
#distribuciones de:

#. cantidad de anémicos
#. cantidad de diabéticos
#. cantidad de fumadores
#. cantidad de muertos

import pandas as pd
import matplotlib.pyplot as plt

archivo = 'C:\\Users\\Lenovo\\OneDrive\\Escritorio\\Maye\\ADA\\PROYECTO_INT\\resultado.csv'
data_df = pd.read_csv(archivo, sep = ",")

# Selecciona solo las columnas relevantes para el histograma
columnas_relevantes = ['is_male', 'has_anaemia', 'has_diabetes', 'is_smoker', 'is_dead']
df_filtrada = data_df[columnas_relevantes]

# Configura la visualización con subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Plotea las gráficas de torta para cada categoría
for i, col in enumerate(df_filtrada.columns[1:]):
    ax = axes[i // 2, i % 2]
    hombres = df_filtrada[df_filtrada['is_male']].groupby(col).size()
    # Plotea las gráficas de torta para hombres y mujeres en el mismo subgráfico
    ax.pie(hombres, labels=hombres.index, autopct='%1.1f%%', startangle=90, radius=0.8, center=(0.25, 0.5))    
    ax.set_title(f'Distribución de {col}')

# Ajusta el diseño
plt.tight_layout()
plt.show()