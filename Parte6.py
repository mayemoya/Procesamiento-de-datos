#Imagina que los datos que procesaste en anteriores etapas del proyecto integrador se van actualizando cada cierto 
#tiempo, (manteniendo el formato) y la url siempre va apuntando a la versión más actual, en este caso conviene 
#tener automatizado el procesamiento en un script que pedas llamar y siempre te dé un csv limpio y listo para su
# análisis.

#Tu tarea en esta etapa del proyecto consiste en crear un script (un archivo .py) que realice todas las operaciones
# vistas hasta ahora (desde el módulo de APIS) que al ejecutarse

#1. Descargue los datos desde una url
#2. Convierta todo a un dataframe
#3. Categorice en grupos
#4. Exporte un csv resultante
#La url no debe estar definida como una constante en el código, en su lugar usa argumentos por terminal 
#(revisar este enlace) para enviarle la url al programa al ejecutarlo.

import sys
import requests
import pandas as pd

def descargar_datos(url):
    try:
        # Realizar la solicitud GET
        respuesta = requests.get(url)
        
        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 200:
            return respuesta.text
        else:
            print(f'Error al realizar la solicitud. Código de estado: {respuesta.status_code}')
            return None
    except Exception as e:
        print(f'Ocurrió un error: {str(e)}')
        return None

def convertir_a_dataframe(datos):
    try:
        # Convertir los datos a un DataFrame
        dataframe = pd.read_csv(pd.compat.StringIO(datos))
        return dataframe
    except pd.errors.EmptyDataError:
        print('Los datos descargados están vacíos.')
        return None
    except Exception as e:
        print(f'Ocurrió un error al convertir a DataFrame: {str(e)}')
        return None

def categorizar_y_exportar_csv(dataframe, archivo_resultante):
    def procesar_datos(dataframe):
        #1. Verificar que no existan valores faltantes
        valores_faltantes = dataframe.isnull().any()
        if valores_faltantes.any():
            print("Existen valores faltantes en las siguientes columnas:")
            print(valores_faltantes[valores_faltantes].index.tolist())
        else:
            print("No hay valores faltantes en el DataFrame.")

        #2. Verificar que no existan filas repetidas
        filas_duplicadas = dataframe.duplicated()
        if filas_duplicadas.any():
            print("Existen filas duplicadas en el DataFrame.")
        else:
            print("No hay filas duplicadas en el DataFrame.")

        # 3. Verificar si existen valores atípicos y eliminarlos

        # Función para identificar y eliminar valores atípicos usando el rango intercuartílico (IQR)
        def eliminar_valores_atipicos(dataframe, columna):
            if dataframe[columna].dtype != bool: 
                q1 = dataframe[columna].quantile(0.25)
                q3 = dataframe[columna].quantile(0.75)
                iqr = q3 - q1
                limite_inferior = q1 - 1.5 * iqr
                limite_superior = q3 + 1.5 * iqr
                df_filtrado = dataframe[(dataframe[columna] >= limite_inferior) & (dataframe[columna] <= limite_superior)]
                return df_filtrado
            else:
                return dataframe

        # Iterar sobre las columnas del DataFrame y aplicar la función para eliminar valores atípicos
        for columna in dataframe.columns:
            df_limpio = eliminar_valores_atipicos(dataframe, columna)

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
    df_procesado = procesar_datos(dataframe)


def main():
    # Verificar si se proporcionó la URL como argumento
    if len(sys.argv) != 2:
        print('Por favor, proporcione la URL como argumento.')
        return

    # Obtener la URL proporcionada como argumento
    url_datos = sys.argv[1]

    # Descargar datos
    datos = descargar_datos(url_datos)

    if datos:
        # Convertir a DataFrame
        df = convertir_a_dataframe(datos)

        if df is not None:
            # Categorizar y exportar a CSV
            categorizar_y_exportar_csv(df, 'datos_procesados.csv')

if __name__ == "__main__":
    main()

#Cuando se ejecute el script, se debe proporcionar la URL como argumento en la terminal 
#Ejemplo: python procesar_datos.py https://ejemplo.com/datos.csv
