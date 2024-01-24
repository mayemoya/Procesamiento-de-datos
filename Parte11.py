#Ahora vamos a empezar a usar el dataset para lo que fue creado, ajustar un modelo de clasificación.

#1. Grafica la distribución de clases (con la librería de tu preferencia) para analizar si este dataset está balanceado o no
#2. Realiza la partición del dataset en conjunto de entrenamiento y test
#3. Esta partición debe ser estratificada. Para lograrlo debes usar el parámetro como stratify=y en la función train_test_split
#4. Ajusta un árbol de decisión y calcula el accuracy sobre el conjunto de test.
#5. Trata de mover los valores de los parámetros para lograr la mayor accuracy que puedas.
#Nota: No olvides eliminar la colúmna categoria_edad.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

archivo = 'C:\\Users\\Lenovo\\OneDrive\\Escritorio\\Maye\\ADA\\PROYECTO_INT\\resultado.csv'
data_df = pd.read_csv(archivo, sep = ",")

# Elimina la columna categoria_edad
df = data_df.drop('categoria_edad', axis=1)

# 1. Grafica la distribución de clases
plt.figure(figsize=(6, 4))
df['is_dead'].value_counts().plot(kind='bar', color=['skyblue', 'red'])
plt.title('Distribución de Clases')
plt.xlabel('is_dead')
plt.ylabel('Cantidad de Instancias')
plt.xticks([0, 1], ['No Fallecido', 'Fallecido'], rotation=0)
plt.show()

# 2. Partición del dataset en conjunto de entrenamiento y test
X = df.drop('is_dead', axis=1)
y = df['is_dead']

# 3. Partición estratificada
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# 4. Ajusta un árbol de decisión
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

# Predicciones en el conjunto de test
y_pred = tree_model.predict(X_test)

# 5. Calcula el accuracy sobre el conjunto de test
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy en el conjunto de test: {accuracy}')
