#Imagina que tenemos datos faltantes en la colúmna de edades, podríamos usar un modelo para estimar los valores 
#faltantes en base a las otras colúmnas.

#Para este laboratorio:

#1. Elimina las colúmnas DEATH_EVENT, age y categoria_edad del dataframe para que sea la matriz X
#2. Ajusta una regresión lineal sobre el resto de colúmnas y usa la colúmna age como vector y
#3. Predice las edades y compara con las edades reales
#4. Calcula el error cuadrático medio.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

archivo = 'C:\\Users\\Lenovo\\OneDrive\\Escritorio\\Maye\\ADA\\PROYECTO_INT\\resultado.csv'
data_df = pd.read_csv(archivo, sep = ",")

# Elimina las columnas DEATH_EVENT, age y categoria_edad
X = data_df.drop(['age', 'categoria_edad'], axis=1)

# La columna 'age' será nuestro vector y
y = data_df['age']

# Divide el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializa y ajusta el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predice las edades en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcula el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)

print(f"Error cuadrático medio: {mse}")
