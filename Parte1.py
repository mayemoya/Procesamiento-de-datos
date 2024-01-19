#El dataset contiene registros médicos de 299 pacientes que padecieron insuficiencia cardíaca durante un 
#período de seguimiento.

#Las 13 características clínicas incluidas en el conjunto de datos son:

#Edad: edad del paciente (años)
#Anemia: disminución de glóbulos rojos o hemoglobina (booleano)
#Presión arterial alta: si el paciente tiene hipertensión (booleano)
#Creatinina fosfoquinasa (CPK): nivel de la enzima CPK en la sangre (mcg/L)
#Diabetes: si el paciente tiene diabetes (booleano)
#Fracción de eyección: porcentaje de sangre que sale del corazón en cada contracción (porcentaje)
#Plaquetas: plaquetas en la sangre (kiloplaquetas/mL)
#Sexo: mujer u hombre (binario)
#Creatinina sérica: nivel de creatinina sérica en la sangre (mg/dL)
#Sodio sérico: nivel de sodio sérico en la sangre (mEq/L)
#Fumar: si el paciente fuma o no (booleano)
#Tiempo: período de seguimiento (días)
#[Objetivo] Evento de fallecimiento: si el paciente falleció durante el período de seguimiento (booleano)

#Tu tarea para esta etapa del proyecto integrador es convertir la lista de edades a un arreglo de NumPy y 
#calcular el promedio de edad de las personas participantes en el estudio.

from datasets import load_dataset
import numpy as np

#Para descargar vamos a usar la librería datasets descargada previamente tal como lo propone el proyecto,
#debemos ejecutar el siguiente framento de código:

dataset = load_dataset("mstz/heart_failure")

#Dataset contiene una estructura similar a un diccionario con particiones de datos y características, 
#debido a que este dataset sólo contiene una partición llamada train, accedemos a todos los registos 
#indexando por esa partición.

data = dataset["train"]

#data es un objeto Dataset que permite indexar por sus atributos como un diccionario. 
#La lista de edades se encuentra en la variable 'age'

edades = data['age']  

# Convertir la lista de edades a un arreglo de NumPy
edades_np = np.array(edades)

# Calcular el promedio de edad
promedio_edad = np.mean(edades_np)

print(f"El promedio de edad de las personas participantes en el estudio es: {promedio_edad:.2f} años.")
