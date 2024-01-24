#Sobre el dataset ya particionado en conjuntos de entrenamiento y test, realiza lo siguiente:
#1. Ajusta un random forest
#2. Calcula su matriz de confusión
#3. Calcula F1-Score y compara con el accuracy
#4. Crees que el accuracy captura completamente el rendimiento del modelo en este caso o no es suficiente?
#5. Trata de cambiar los valores de los parámetros del random forest para conseguir el mejor resultado que puedas.
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

archivo = 'C:\\Users\\Lenovo\\OneDrive\\Escritorio\\Maye\\ADA\\PROYECTO_INT\\resultado.csv'
data_df = pd.read_csv(archivo, sep = ",")

# Elimina la columna categoria_edad
df = data_df.drop('categoria_edad', axis=1)

# Partición del dataset en conjunto de entrenamiento y test
X = df.drop('is_dead', axis=1)
y = df['is_dead']

# Partición estratificada
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Ajusta un árbol de decisión
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

# Predicciones en el conjunto de test
y_pred = tree_model.predict(X_test)

# 1. Ajusta un Random Forest
random_forest_model = RandomForestClassifier(random_state=42)
random_forest_model.fit(X_train, y_train)

# Predicciones en el conjunto de test
y_pred_rf = random_forest_model.predict(X_test)

# 2. Calcula la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred_rf)
print("Matriz de Confusión:")
print(conf_matrix)

# 3. Calcula F1-Score
f1 = f1_score(y_test, y_pred_rf)
print(f'F1-Score: {f1}')

# Calcula el accuracy
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f'Accuracy en el conjunto de test (Random Forest): {accuracy_rf}')

print("Considero que el 83.33 de las instancias se clasificaron correctamente y Un F1-Score de 0.6875 sugiere un equilibrio entre precisión y exhaustividad.")