#Imagina que no tuvieramos el acceso fácil de estos datos a través de la librería y tuvieramos que descargar 
#los datos usando requests.

#Los datos son accesibles en esta dirección

#Realiza un GET request para descargarlos y escribe la respuesta como un archivo de texto plano con extensión csv 
#(no necesitas pandas para esto, sólo manipulación de archivos nativa de Python)
#Agrupa el código para esto en una función reutilizable que reciba como argumento la url.


import requests

def descargar_y_guardar_csv(url, nombre_archivo):
    try:
        # Realizar la solicitud GET
        respuesta = requests.get(url)
        
        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 200:
            # Guardar la respuesta en un archivo CSV
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(respuesta.text)
            print(f'Los datos fueron descargados y guardados en {nombre_archivo} exitosamente.')
        else:
            print(f'Error al realizar la solicitud. Código de estado: {respuesta.status_code}')
    except Exception as e:
        print(f'Ocurrió un error: {str(e)}')

# Ejemplo de uso
url_datos = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
nombre_archivo_salida = 'datos_descargados.csv'

descargar_y_guardar_csv(url_datos, nombre_archivo_salida)
