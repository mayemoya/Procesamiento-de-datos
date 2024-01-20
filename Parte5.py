import pandas as pd
import numpy as np
from datasets import load_dataset
#Para descargar vamos a usar la librería datasets descargada previamente tal como lo propone el proyecto,
#debemos ejecutar el siguiente framento de código:

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
# Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.

df = pd.DataFrame(data)


def procesar_datos(df):
    #1. Verificar que no existan valores faltantes
    valores_faltantes = df.isnull().any()
    if valores_faltantes.any():
        print("Existen valores faltantes en las siguientes columnas:")
        print(valores_faltantes[valores_faltantes].index.tolist())
    else:
        print("No hay valores faltantes en el DataFrame.")

    #2. Verificar que no existan filas repetidas
    filas_duplicadas = df.duplicated()
    if filas_duplicadas.any():
        print("Existen filas duplicadas en el DataFrame.")
    else:
        print("No hay filas duplicadas en el DataFrame.")

    # 3. Verificar si existen valores atípicos y eliminarlos

    # Función para identificar y eliminar valores atípicos usando el rango intercuartílico (IQR)
    def eliminar_valores_atipicos(df, columna):
        if df[columna].dtype != bool: 
            q1 = df[columna].quantile(0.25)
            q3 = df[columna].quantile(0.75)
            iqr = q3 - q1
            limite_inferior = q1 - 1.5 * iqr
            limite_superior = q3 + 1.5 * iqr
            df_filtrado = df[(df[columna] >= limite_inferior) & (df[columna] <= limite_superior)]
            return df_filtrado
        else:
            return df

    # Iterar sobre las columnas del DataFrame y aplicar la función para eliminar valores atípicos
    for columna in df.columns:
        df_limpio = eliminar_valores_atipicos(df, columna)

    # 4. Crear una columna que categorice por edades: 0-12: Niño, 13-19: Adolescente, 20-39: Joven adulto,
    #40-59: Adulto, 60-...: Adulto mayor

    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Joven adulto', 'Adulto', 'Adulto mayor']

    df_limpio['categoria_edad'] = pd.cut(df_limpio['age'], bins=bins, labels=labels, right=False)

    # Mostrar el DataFrame con la nueva columna
    print(df_limpio)

    #5. Guardar el resultado como csv. Encapsula toda la lógica anterior en una función que reciba 
    #un dataframe como entrada.
    df_limpio.to_csv('resultado.csv', index=False)

    return df_limpio


# Llamada a la función para procesar los datos
df_procesado = procesar_datos(df)



