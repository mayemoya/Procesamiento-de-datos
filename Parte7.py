#Una vez tenemos los datos exportados por nuestro script de ETL, podemos proceder a realizar gráficas de análisis. 
#En esta etapa del proyecto usa matplotlib para:

#1. Graficar la distribución de edades con un histograma
#2. Graficar histogramas agrupado por hombre y mujer:
#. cantidad de anémicos
#. cantidad de diabéticos
#. cantidad de fumadores
#. cantidad de muertos

import pandas as pd
import matplotlib.pyplot as plt

archivo = 'C:\\Users\\Lenovo\\OneDrive\\Escritorio\\Maye\\ADA\\PROYECTO_INT\\resultado.csv'
data_df = pd.read_csv(archivo, sep = ",")

#1. Graficar la distribución de edades con un histograma
frecuencia_palabras = data_df['categoria_edad'].value_counts()
frecuencia_palabras.plot(kind="bar", color = ["blue", "green"])
plt.title('Distribucion de edades')
plt.xlabel('Categorias')
plt.ylabel('Cantidad')
plt.show()

#2. Graficar histogramas agrupado por hombre y mujer: cantidad de anémicos, cantidad de diabéticos, 
#cantidad de fumadores, cantidad de muertos

# Selecciona solo las columnas relevantes para el histograma
columnas_relevantes = ['is_male', 'has_anaemia', 'has_diabetes', 'is_smoker', 'is_dead']
df_filtrada = data_df[columnas_relevantes]

# Plotea los histogramas agrupados por género para cada categoría
df_filtrada.groupby('is_male')[['has_anaemia', 'has_diabetes', 'is_smoker', 'is_dead']].sum().T.plot(kind='bar', color = ["blue", "red"], position=0, width=0.4)

# Configura los detalles del gráfico
plt.title('Histograma agrupado por sexo')
plt.xlabel('Categorías')
plt.ylabel('Cantidad')
plt.legend(title='Género', bbox_to_anchor=(1, 1))

plt.show()

