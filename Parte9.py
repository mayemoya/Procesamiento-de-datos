import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px

archivo = 'C:\\Users\\Lenovo\\OneDrive\\Escritorio\\Maye\\ADA\\PROYECTO_INT\\resultado.csv'
data_df = pd.read_csv(archivo, sep = ",")

# Elimina las columnas no necesarias
columnas_no_necesarias = [ 'categoria_edad']
X = data_df.drop(columns=columnas_no_necesarias).values

# Exporta un array unidimensional de la columna objetivo DEATH_EVENT
y = data_df['is_dead'].values

# Realiza la reducción de dimensionalidad
X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

# Crea un DataFrame con las coordenadas reducidas y la etiqueta DEATH_EVENT
df_embedded = pd.DataFrame({'Dimension_1': X_embedded[:, 0], 'Dimension_2': X_embedded[:, 1], 'Dimension_3': X_embedded[:, 2], 'is_dead': y})

# Crea el gráfico de dispersión 3D con Plotly
fig = px.scatter_3d(df_embedded, x='Dimension_1', y='Dimension_2', z='Dimension_3', color='is_dead', 
                    labels={'Dimension_1': 'Dimensión 1', 'Dimension_2': 'Dimensión 2', 'Dimension_3': 'Dimensión 3'},
                    title='Gráfico de dispersión 3D con t-SNE',
                    color_discrete_map={0: 'blue', 1: 'red'})  # Asigna colores a las clases

# Muestra el gráfico
fig.show()